from turtle import Turtle
from turtle import Screen
from base import Shape
from .utils import Utils


class _GameWindow:

    _game_window = None
    s = Screen()

    def __init__(self):
        self.s.setup(0.5, 0.75)
        self.s.title('贪吃蛇')
        self.canvwidth = self.s.window_width()
        self.canvheight = self.s.window_height()
        self.s.getcanvas().bind('<Configure>', self.window_resize)
        self.eraser = Turtle()
        Utils.turtle_init(self.eraser)

    def window_resize(self, event):
        self.canvwidth = self.s.window_width()
        self.canvheight = self.s.window_height()

    def clear_window(self):
        '''清空屏幕

        注：turtle内置的clearscreen()函数会对Tkinter全局的状态有影响
        '''
        Shape.rect(t=self.eraser,
                   x=-self.canvwidth / 2,
                   y=self.canvheight / 2,
                   w=self.canvwidth,
                   h=self.canvheight,
                   anchor='tl',
                   border=False,
                   fill=True,
                   fillcolor='#ffffff')


def GameWindow():
    if _GameWindow._game_window is None:
        _GameWindow._game_window = _GameWindow()
    return _GameWindow._game_window
