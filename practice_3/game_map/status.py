from random import randint
from frame import Collision


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
    GROUP_MAP1 = 'map1'
    NAME_SNAKE = 'snake'
    NAME_FOOD = 'food'

    def ondestroy(self):
        _Status._status = None

    def get_collision(self):
        return self.collision

    def refresh_food(self):
        while True:
            col = randint(0, self.CELL_COLUMN_NUM - 1)
            row = randint(0, self.CELL_ROW_NUM - 1)
            if self.map1[row][col] != self.SNAKE:
                self.map1[row][col] = self.FOOD
                self.food_col = col
                self.food_row = row
                break

    def __init__(self):

        self.map1 = (lambda val, col, row:
                     [[val] * col for _ in range(row)])(self.BLANK,
                                                        self.CELL_COLUMN_NUM,
                                                        self.CELL_ROW_NUM)
        self.collision = Collision()
        self.score = 0
        self.wall_enable = True
        self.snake_list = []
        self.snake_speed = 5    # 每秒移动单位数
        self.snake_len = 6
        self.snake_dir = 'r'
        # 设置蛇位置
        self.snake_head_col = int(self.CELL_COLUMN_NUM / 2)
        self.snake_head_row = int(self.CELL_ROW_NUM / 2)
        col = self.snake_head_col
        row = self.snake_head_row
        for i in range(self.snake_len):
            self.map1[row][col - i] = self.SNAKE
        # 设置食物位置
        self.refresh_food()


def Status():
    if _Status._status is None:
        _Status._status = _Status()
    return _Status._status
