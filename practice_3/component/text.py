from turtle import Turtle
from frame import GameWindow
from frame import Utils


class Text:

    window = GameWindow()
    t = Turtle()

    def __init__(self,
                 text='Text',
                 x=0, y=0, align='center',
                 font: tuple[str, int, str] = ('Arial', 8, 'normal')):
        self.text = text
        self.x = x
        self.y = y
        self.align = align
        self.font = font
        Utils.turtle_init(self.t)
        self._init()

    def _init(self):
        self._draw()

    def _draw(self):
        self.t.setpos(self.x, self.y)
        self.t.write(self.text, False, self.align, self.font)
