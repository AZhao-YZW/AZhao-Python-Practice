from turtle import Turtle
from turtle import Screen
from frame import MotionEvent
from frame import GameWindow
from frame import Utils
from component import Button, Text, Mouse
from base import Shape
from frame import Timer
from .wall import Wall
from .food import Food
from .snake import Snake
from .status import Status


class Map1:

    def update(self, cell_list: list[list[int, int, int]]):
        '''cell_list: 需要改变的格子列表，(col, row, type) 第col列第row行type类型'''
        start_x = -self.status.WALL_WIDTH / 2
        start_y = self.status.WALL_HEIGHT / 2
        for cell in cell_list:
            col = cell[0]
            row = cell[1]
            cell_type = cell[2]
            if cell_type == self.status.BLANK:
                color = self.status.BLANK_COLOR
            elif cell_type == self.status.FOOD:
                color = self.status.FOOD_COLOR
            elif cell_type == self.status.SNAKE:
                color = self.status.SNAKE_COLOR
            else:
                raise ValueError('type is wrong.')

            self.status.map1[row][col] = cell_type
            Shape.rect(t=self.t,
                       x=start_x + self.status.CELL_SIDE * col,
                       y=start_y - self.status.CELL_SIDE * row,
                       w=self.status.CELL_SIDE,
                       h=self.status.CELL_SIDE,
                       anchor='tl',
                       border=True,
                       bordercolor='#ffffff',
                       borderwidth=2,
                       fill=True,
                       fillcolor=color)

    def _score_inc(self):
        self.status.score += 1
        self.text_num.set_text(str(self.status.score))

    def __init__(self, return_menu):
        self.mouse = Mouse()
        self.s = Screen()
        self.window = GameWindow()
        self.motion_event = MotionEvent()
        self.status = Status()
        self.t = Turtle()
        Utils.turtle_init(self.t)
        self._return_menu = return_menu
        self._map1_init()

    def _map1_init(self):
        self.text_title = Text('贪吃蛇',
                               0, 360, 140, 50, 'center',
                               ('Arial', 24, 'normal'))
        self.text_score = Text('分数：',
                               220, 360, 80, 30, 'center',
                               ('Arial', 16, 'normal'))
        self.text_num = Text('0',
                             280, 360, 40, 30, 'center',
                             ('Arial', 16, 'normal'))
        self.btn_exit = Button('返回主菜单',
                               -400, 370, 140, 30, 'center',
                               ('Arial', 16, 'normal'))
        self.btn_exit.onclick(self._map1_exit)
        self.wall = Wall()
        self._draw_backgroud()
        self.food = Food(self.update, self._score_inc)
        self.snake = Snake(self.update)
        # init_cell_list = [(x, y, self.status.FOOD)
        #                   for x in range(self.status.CELL_COLUMN_NUM)
        #                   for y in range(self.status.CELL_ROW_NUM)]
        # self.update(init_cell_list)

    def _draw_backgroud(self):
        # 画出空白背景
        Shape.rect(t=self.t,
                   x=-self.status.WALL_WIDTH / 2,
                   y=self.status.WALL_HEIGHT / 2,
                   w=self.status.WALL_WIDTH,
                   h=self.status.WALL_HEIGHT,
                   anchor='tl',
                   border=False,
                   fill=True,
                   fillcolor=self.status.BLANK_COLOR)
        # 使用白线分割出格子
        line_y = -self.status.WALL_HEIGHT / 2
        line_x = -self.status.WALL_WIDTH / 2
        for i in range(self.status.CELL_COLUMN_NUM + 1):
            Shape.line(t=self.t,
                       x=-self.status.WALL_WIDTH / 2,
                       y=line_y + self.status.CELL_SIDE * i,
                       len=self.status.WALL_WIDTH,
                       orient='h',
                       bordercolor='#ffffff',
                       borderwidth=2)
            Shape.line(t=self.t,
                       x=line_x + self.status.CELL_SIDE * i,
                       y=self.status.WALL_HEIGHT / 2,
                       len=self.status.WALL_HEIGHT,
                       orient='v',
                       bordercolor='#ffffff',
                       borderwidth=2)

    def _map1_destroy(self):
        self.snake.ondestroy()
        self.btn_exit.ondestroy()
        self.status.collision.delete(self.status.GROUP_MAP1)
        self.status.ondestroy()
        self.window.clear_window()

    def _map1_exit(self):
        self._map1_destroy()
        self._return_menu()
