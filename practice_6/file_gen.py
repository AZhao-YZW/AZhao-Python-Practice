'''
使用Python实现一个命令行工具
    基本功能:
    1. 按照一定的命名规则，批量创建文件
    2. 批量对文件改名
    3. 根据文件名生成文件内容
    4. 按照一定的规则，批量修改文件内容

    实现要求:
    1. 满足基本功能
    2. 命令行工具能够按照一定规则传入参数
    3. 对不合理的输入做拦截，提高工具的可靠性
'''
import os
import time

dir = 'gen_dir'

def gen_dir():
    if not os.path.exists(dir):
        os.mkdir(dir)

def gen_file():
    print('file name rule: file_num_time')
    for num in range(10):
        rule = [
            'file' + '_',
            str(num).zfill(3) + '_',
            time.strftime('%Y%m%d%H%M%S', time.localtime()),
            '.txt'
        ]
        file_name = dir + os.sep
        for r in rule:
            file_name = file_name + r
        with open(file_name, 'w') as f:
            content = [
                'num: ' + str(num).zfill(3),
                'time: ' + time.strftime('%Y%m%d%H%M%S', time.localtime())
            ]
            for line in content:
                print(line, file=f)


if __name__ == '__main__':
    '''
    file_gen.py [-h/--help] [-d/--dir] [-p/--prefix] [-n/--num] [-t/--time]
    -h: 获取工具说明
    -d: -d dir_name, 指定工具操作的目录，默认为 gen_dir
    -p: -p file, 指定生成文件名前缀，默认为 file
    -n: 生成文件名中包含编号，默认不包含
    -t: 生成文件名中包含时间，默认不包含
    -c: 批量修改文件内容，此参数必须单独使用
    '''
    gen_dir()
    gen_file()