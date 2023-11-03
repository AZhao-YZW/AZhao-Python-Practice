from turtle import Turtle
from frame import Utils
from base import Shape
from .status import Status


class Wall:

    def enable(self):
        self.status.wall_enable = True

    def disable(self):
        self.status.wall_enable = False

    def __init__(self):
        self.status = Status()
        self.t = Turtle()
        Utils.turtle_init(self.t)
        self._draw()

    def _draw(self):
        Shape.rect(t=self.t,
                   x=-self.status.wall_width / 2 - 5,
                   y=self.status.wall_height / 2 + 5,
                   w=self.status.wall_width + 10,
                   h=self.status.wall_height + 10,
                   anchor='tl',
                   border=True,
                   bordercolor='#000000',
                   borderwidth=10,
                   fill=True,
                   fillcolor='#dddddd')
        # 使用白线分割出格子
        line_y = -self.status.wall_height / 2
        line_x = -self.status.wall_width / 2
        for i in range(self.status.CELL_COLUMN_NUM + 1):
            Shape.line(t=self.t,
                       x=-self.status.wall_width / 2,
                       y=line_y + self.status.CELL_SIDE * i,
                       len=self.status.wall_width,
                       orient='h',
                       bordercolor='#ffffff',
                       borderwidth=2)
            Shape.line(t=self.t,
                       x=line_x + self.status.CELL_SIDE * i,
                       y=self.status.wall_height / 2,
                       len=self.status.wall_height,
                       orient='v',
                       bordercolor='#ffffff',
                       borderwidth=2)
