from turtle import Turtle
from frame import Utils
from base import Shape

class Wall:

    def enable(self):
        self.enable = True

    def disable(self):
        self.enable = False

    def __init__(self, w=700, h=700, enable=True):
        self.w = w
        self.h = h
        self.enable = enable
        self.t = Turtle()
        self._wall_init()

    def _wall_init(self):
        Utils.turtle_init(self.t)
        self._draw()

    def _draw(self):
        Shape.rect(t=self.t,
                   x=-self.w / 2,
                   y=self.h / 2,
                   w=self.w,
                   h=self.h,
                   anchor='tl',
                   border=True,
                   bordercolor='#000000',
                   borderwidth=10,
                   fill=False)
