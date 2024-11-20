from collections.abc import Callable
from turtle import Turtle
from frame import MotionEvent, MouseLPressEvent
from frame import GameWindow
from frame import Utils
from base import Shape


class Button:

    window = GameWindow()
    _motion_event = MotionEvent()
    _mouse_left_press_event = MouseLPressEvent()
    t = Turtle()

    def onclick(self, callback: Callable[[None], None]):
        self._callback = callback

    def ondestroy(self):
        self._motion_event.unbind(self._movein_listener)
        self._mouse_left_press_event.unbind(self._onclick_listener)

    def __init__(self,
                 text='Button',
                 x=0, y=0, w=100, h=50, align='center',
                 font: tuple[str, int, str] = ('Arial', 8, 'normal')):
        self.text = text
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.align = align
        self.font = font
        Utils.turtle_init(self.t)
        self._instance_var_init()
        self._init()

    def _instance_var_init(self):
        self.inter_times = 0
        self.move_in = False
        self.move_out = True
        self.mouse_down = False
        self._callback = None

    def _init(self):
        self._draw()
        self._motion_event.bind(self._movein_listener)
        self._mouse_left_press_event.bind(self._onclick_listener)

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

    def _is_in_btn(self, sx, sy):
        canvwidth = self.window.canvwidth
        canvheight = self.window.canvheight
        x, y = Utils.axis_adapter(sx, sy, canvwidth, canvheight)
        tl_x, tl_y = self._get_tl_axis()
        if (x > tl_x and x < tl_x + self.w and y < tl_y and y > tl_y - self.h):
            self.inter_times += 1
            if self.inter_times > 20:   # 防止按键状态切换过快
                return True
            else:
                return False
        else:
            return False

    def _is_move_in(self, x, y):
        if self._is_in_btn(x, y):
            if self.move_in is False:
                self.move_in = True
                return True
        else:
            self.move_in = False
        return False

    def _is_move_out(self, x, y):
        if self._is_in_btn(x, y):
            self.move_out = False
        else:
            if self.move_out is False:
                self.move_out = True
                self.inter_times = 0
                return True
        return False

    def _movein_listener(self, event):
        if self._is_move_in(event.x, event.y):
            self._draw('#dddddd')

        if self._is_move_out(event.x, event.y):
            self._draw('#ffffff')

    def _onclick_listener(self, event):
        if self._is_in_btn(event.x, event.y):
            self._callback()
