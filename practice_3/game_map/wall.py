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
                   x=-self.status.WALL_WIDTH / 2 - 5,
                   y=self.status.WALL_HEIGHT / 2 + 5,
                   w=self.status.WALL_WIDTH + 10,
                   h=self.status.WALL_HEIGHT + 10,
                   anchor='tl',
                   border=True,
                   bordercolor='#000000',
                   borderwidth=10,
                   fill=False)
