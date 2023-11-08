from turtle import Turtle
from frame import GameWindow
from frame import Utils
from base import Shape


class Text:

    window = GameWindow()
    t = Turtle()

    def set_text(self, text: str):
        self.text = text
        self._draw('#ffffff')

    def __init__(self,
                 text='Text',
                 x=0, y=0, w=100, h=50, align='center',
                 font: tuple[str, int, str] = ('Arial', 8, 'normal')):
        '''w, h 参数仅在需更新文字时，确定清屏范围'''
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.align = align
        self.font = font
        Utils.turtle_init(self.t)
        self._init()

    def _init(self):
        self._draw('#ffffff')

    def _get_tl_axis(self):
        '''input (x, y) cast to top-left anchor (x, y)'''
        if self.align == 'center':
            return self.x - self.w / 2, self.y + self.h
        elif self.align == 'left':
            return self.x, self.y + self.h
        elif self.align == 'right':
            return self.x - self.w, self.y + self.h

    def _draw(self, color=None):
        if color:
            tl_x, tl_y = self._get_tl_axis()
            Shape.rect(t=self.t,
                       x=tl_x,
                       y=tl_y,
                       w=self.w,
                       h=self.h,
                       anchor='tl',
                       border=False,
                       fill=True,
                       fillcolor=color)
        self.t.setpos(self.x, self.y)
        self.t.write(self.text, False, self.align, self.font)
