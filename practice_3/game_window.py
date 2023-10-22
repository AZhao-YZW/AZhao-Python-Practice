from turtle import Turtle
from turtle import Screen


class _GameWindow:

    _game_window = None
    s = Screen()
    canvwidth: int
    canvheight: int

    def __init__(self):
        self.s.setup(0.5, 0.75)
        self.game_window_init()

    def game_window_init(self):
        self.s.title('贪吃蛇')
        self.canvwidth = self.s.window_width()
        self.canvheight = self.s.window_height()
        self.s.getcanvas().bind('<Configure>', self.window_resize)

    def window_resize(self, event):
        self.canvwidth = self.s.window_width()
        self.canvheight = self.s.window_height()

def GameWindow():
    if _GameWindow._game_window is None:
        _GameWindow._game_window = _GameWindow()
    return _GameWindow._game_window