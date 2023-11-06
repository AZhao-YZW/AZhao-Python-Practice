from collections.abc import Callable


class Collision:
    '''碰撞检测类

    将需要进行碰撞检测的一组对象，注册到同一碰撞检测组中，
    并为每个碰撞对象注册碰撞对象名、碰撞响应函数
    '''

    def __init__(self):
        self.group_list: list[dict['group': str,
                                   'name': list[list[str, Callable[[None], None]]]]] = []

    def register(self, group: str, name: str, callback: Callable[[None], None]):
        for g in self.group_list:
            if g['group'] == group:
                break
        else:
            self.group_list.append({'group': group, 'name': []})

        for g in self.group_list:
            if g['group'] == group and [name, callback] not in g['name']:
                g['name'].append([name, callback])

    def delete(self, group: str, name: str = None, callback: Callable[[None], None] = None):
        '''1个参数: 删除group; 2个参数: 删除group中name'''
        if name is None:
            for g in self.group_list:
                if g['group'] == group:
                    self.group_list.remove(g)
        else:
            for g in self.group_list:
                if g['group'] == group and [name, callback] in g['name']:
                    g['name'].remove([name, callback])

    def notify(self, group: str, name: str):
        '''碰撞由主动碰撞方发起，通知给name对象，使其执行对应函数'''
        for g in self.group_list:
            if g['group'] == group:
                for n in g['name']:
                    if n[0] == name:
                        n[1]()
