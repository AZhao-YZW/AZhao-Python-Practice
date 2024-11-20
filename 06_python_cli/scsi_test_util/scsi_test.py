import os
import argparse, argcomplete
import paramiko
from typing import List, Dict, Callable

#------------------ 数据类 ------------------#
class ScsiTestConfig:
    scsi_test_params = {
        '--ssh': {
            'action': 'store',
            'metavar': 'IP:PORT:USER:PASSWD',
            'default': 'test',
            'help': 'default: test(means only print at local), example: 172.27.78.245:22:azhao:yzw2823487'
        },
        '--dev': {
            'action': 'store',
            'metavar': 'DEVICE',
            'default': 'sdb',
            'help': 'default: sdb'
        },
        '--sudo': {'action': 'store_true'},
        '--all':           {'action': 'store_true'},
        '--sg_inq':        {'action': 'store_true'},
        '--sg_modes_6':    {'action': 'store_true'},
        '--sg_modes_10':   {'action': 'store_true'},
        '--sg_wr_mode_6':  {'action': 'store_true'},
        '--sg_wr_mode_10': {'action': 'store_true'},
        '--sg_luns':       {'action': 'store_true'},
        '--sg_requests':   {'action': 'store_true'},
        '--sg_turs':       {'action': 'store_true'},
        '--sg_senddiag':   {'action': 'store_true'},
        '--sg_vpd':        {'action': 'store_true'},
    }

    sg3_utils_test_table = {
        'sg_inq': {
            'base_cmd': 'sg_inq',
            'params': ['--vpd', '--page'],
            'values': [
                [[True], ['0x00', '0x83']],
                [[False], [False]]
            ]
        },
        'sg_modes_6': {
            'base_cmd': 'sg_modes -6',
            'params': ['--dbd', '--control', '--page'],
            'values': [
                [[True, False], [0, 1, 2, 3], ['0x0A', '0x08', '0x3F,0x00']]
            ]
        },
        'sg_modes_10': {
            'base_cmd': 'sg_modes',
            'params': ['--llbaa', '--dbd', '--control', '--page'],
            'values': [
                [[True, False], [True, False], [0, 1, 2, 3], ['0x0A', '0x08', '0x3F,0x00']]
            ]
        },
        'sg_wr_mode_6': {
            'base_cmd': 'sg_wr_mode -6',
            'params': ['--rtd', '--save', '--page'],
            'values': [
                [[True, False], [True, False], ['0x0A', '0x08', '0x3F,0x00']]
            ]
        },
        'sg_wr_mode_10': {
            'base_cmd': 'sg_wr_mode',
            'params': ['--rtd', '--save', '--page'],
            'values': [
                [[True, False], [True, False], ['0x0A', '0x08', '0x3F,0x00']]
            ]
        },
        'sg_luns': {
            'base_cmd': 'sg_luns',
            'params': [],
            'values': []
        },
        'sg_requests': {
            'base_cmd': 'sg_requests',
            'params': ['--desc'],
            'values': [
                [[True, False]]
            ]
        },
        'sg_turs': {
            'base_cmd': 'sg_turs',
            'params': [],
            'values': []
        },
        'sg_senddiag': {
            'base_cmd': 'sg_senddiag',
            'params': ['--selftest', '--pf', '--test', '--doff', '--uoff'],
            'values': [
                [[0], [True, False], [True], [True, False], [True, False]],
                [[1, 2, 4, 5, 6], [True, False], [False], [False], [False]]
            ]
        },
    }

    sg3_utils_extern_table = {
        'sg_vpd': {
            'base_cmd': 'sg_vpd',
            'params': ['--all'],
            'values': [
                [[True, False]]
            ]
        },
    }

# 全局配置，不可变
config = ScsiTestConfig()

#------------------ ssh连接主机 ------------------#
class SshClient:
    _ssh_client = None
    _ssh: str = None

    def __init__(self, ssh: str):
        self._ssh = ssh
        self._ssh_client = paramiko.SSHClient()

    def _input_print(self, input: str):
        print('+ ' + input, flush=True)

    def _ssh_connect(self):
        self._ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        hostname, port, username, password = self._ssh.split(':')
        self._ssh_client.connect(hostname, port, username, password)
    
    def _ssh_close(self):
        self._ssh_client.close()

    def _ssh_send(self, input: str):
        _, stdout, stderr = self._ssh_client.exec_command(input)
        output = stdout.read().decode()
        print(output, end='', flush=True)
        error = stderr.readline()
        if '[sudo]' not in error:
            print(error, end='', flush=True)
        error = stderr.read().decode()
        print(error, end='', flush=True)

    def connect(self):
        if self._ssh == 'test':
            return
        self._ssh_connect()

    def close(self):
        if self._ssh == 'test':
            return
        self._ssh_close()

    def send(self, display: str, exec: str):
        self._input_print(display)
        if self._ssh == 'test':
            return
        self._ssh_send(exec)

#------------------ 命令行参数 ------------------#
class ArgsParser:
    def gen_args(self):
        parser = argparse.ArgumentParser(description='sg_utils cmd batch execute tool')
        for param, value_list in config.scsi_test_params.items():
            parser.add_argument(param, **value_list)
        return parser.parse_args()

#------------------ sg3_utils 命令 ------------------#
class Sg3UtilsCmd:
    _dev: str = None
    _send_func: Callable[[str, str], None] = None
    _sudo: str = None

    def __init__(self, dev: str, send_func: Callable[[str, str], None], sudo: bool, ssh: str):
        self._dev = '/dev/' + dev
        self._send_func = send_func
        self._sudo = 'echo "{}" | sudo -S '.format(ssh.split(':')[3]) if sudo else ''

    def _exec_cmd(self, cmd: str):
        self._send_func(cmd, self._sudo + cmd)

    def _gen_cmd_list(self, base_cmd: str, param: Dict) -> List[str]:
        def _get_append_param(key, value):
            if value is True:
                append_param = '{} '.format(key)
            elif value is False:
                append_param = ''
            else:
                append_param = '{}={} '.format(key, value)
            return append_param
        
        cmd_list: List[str] = []
        new_cmd_list: List[str] = []
        cmd_list.append('{} {} '.format(base_cmd, self._dev))
        for key, value_list in param.items():
            for cmd in cmd_list:
                for value in value_list:
                    new_cmd = cmd + _get_append_param(key, value)
                    new_cmd_list.append(new_cmd)
            cmd_list = new_cmd_list
            new_cmd_list = []
        return cmd_list

    def _exec_cmd_list(self, base_cmd: str, param_list: List[Dict]):
        if param_list == []:
            cmd = '{} {} '.format(base_cmd, self._dev)
            self._exec_cmd(cmd)
            return
        cmd_list: List[str] = []
        for param in param_list:
            cmd_list = cmd_list + self._gen_cmd_list(base_cmd, param)
        for cmd in cmd_list:
            self._exec_cmd(cmd)

    def _exec_test(self, info: Dict):
        p_set_list = []
        value_list: List = info['values']
        p_name_list: List[str] = info['params']
        base_cmd = info['base_cmd']
        for values in value_list:
            p_set = {}
            for index, p_name in enumerate(p_name_list):
                p_set[p_name] = values[index]
            p_set_list.append(p_set)
        self._exec_cmd_list(base_cmd, p_set_list)

    def _all_test(self):
        for cmd, info in config.sg3_utils_test_table.items():
            self._exec_test(info)

    def _single_test(self, args_dict: Dict, sg3_cmd_table: Dict):
        for cmd, info in sg3_cmd_table.items():
            if cmd in args_dict and args_dict[cmd] is True:
                self._exec_test(info)

    def sg_cmd(self, args_dict: Dict):
        if args_dict['all'] is True:
            self._all_test()
            return
        self._single_test(args_dict, config.sg3_utils_test_table)
        self._single_test(args_dict, config.sg3_utils_extern_table)

if __name__ == '__main__':
    args_parser = ArgsParser()
    args = args_parser.gen_args()

    ssh_client = SshClient(args.ssh)
    ssh_client.connect()

    sg3_utils_cmd = Sg3UtilsCmd(args.dev, ssh_client.send, args.sudo, args.ssh)
    sg3_utils_cmd.sg_cmd(vars(args))