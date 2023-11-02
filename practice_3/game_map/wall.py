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
                   x=-self.status.wall_width / 2,
                   y=self.status.wall_height / 2,
                   w=self.status.wall_width,
                   h=self.status.wall_height,
                   anchor='tl',
                   border=True,
                   bordercolor='#000000',
                   borderwidth=10,
                   fill=False)
