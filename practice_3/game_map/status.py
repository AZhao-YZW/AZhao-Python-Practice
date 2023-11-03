class _Status:
    '''游戏状态管理'''
    _status = None

    CELL_SIDE = 20
    CELL_ROW_NUM = 35
    CELL_COLUMN_NUM = 35

    score = 0
    wall_width = CELL_SIDE * CELL_COLUMN_NUM
    wall_height = CELL_SIDE * CELL_ROW_NUM
    wall_enable = True
    snake_speed = 2    # 每秒移动单位数
    snake_len = 3


def Status():
    if _Status._status is None:
        _Status._status = _Status()
    return _Status._status
