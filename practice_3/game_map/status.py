class _Status:
    '''游戏状态管理'''
    _status = None

    CELL_SIDE = 20
    CELL_ROW_NUM = 35
    CELL_COLUMN_NUM = 35
    BLANK = 0
    FOOD = 1
    SNAKE = 2
    BLANK_COLOR = '#dddddd'
    FOOD_COLOR = '#dd0000'
    SNAKE_COLOR = '#000000'
    WALL_WIDTH = CELL_SIDE * CELL_COLUMN_NUM
    WALL_HEIGHT = CELL_SIDE * CELL_ROW_NUM

    def ondestroy(self):
        _Status._status = None

    def __init__(self):

        self.map1 = (lambda val, col, row:
                     [[val] * col for _ in range(row)])(self.BLANK,
                                                        self.CELL_COLUMN_NUM,
                                                        self.CELL_ROW_NUM)
        self.score = 0
        self.wall_enable = True
        self.snake_list = []
        self.snake_speed = 2    # 每秒移动单位数
        self.snake_len = 6
        self.snake_dir = 'r'
        self.snake_head_col = int(self.CELL_COLUMN_NUM / 2)
        self.snake_head_row = int(self.CELL_ROW_NUM / 2)


def Status():
    if _Status._status is None:
        _Status._status = _Status()
        print('#############')
    return _Status._status
