class _Status:
    '''游戏状态管理'''
    _status = None

    score = 0
    wall_width = 700
    wall_height = 700
    wall_enable = True
    snake_speed = 10    # 每秒移动单位数
    snake_len = 1


def Status():
    if _Status._status is None:
        _Status._status = _Status()
    return _Status._status
