from turtle import Turtle
from event import MotionEvent
from game_window import GameWindow
from util import *

MOUSE_LEFT_DOWN = 8
MOTION_EVENT = 6
BUTTON_PRESS_EVENT = 4

class Button:

    t = Turtle()
    w = GameWindow()
    motion_event = MotionEvent()
    mouse: Turtle
    move_in = False
    move_out = True
    mouse_down = False
    text: str
    pos: dict[str, int]
    size: dict[str, int]
    font: tuple[str, int, str]
    _callback = None

    def onclick(self, callback):
        self._callback = callback

    def ondestroy(self):
        self.motion_event.unbind(self._movein_listener)
        self.motion_event.unbind(self._onclick_listener)

    def __init__(self,
                 mouse,
                 text='Button',
                 x=0, y=0, w=100, h=50,
                 font=('Arial', 8, 'normal')):
        self.mouse = mouse
        self.text = text
        self.pos = {'x': x, 'y': y}
        self.size = {'w': w, 'h': h}
        self.font = font
        self._init()

    def _init(self):
        self._turtle_init()
        self._draw()
        self.motion_event.bind(self._movein_listener)
        self.motion_event.bind(self._onclick_listener)

    def _turtle_init(self):
        self.t.hideturtle()
        self.t.penup()
        self.t.speed(0)

    def _draw(self, color=None):
        if color:
            self.t.setpos(self.pos['x'] - self.size['w'] / 2, self.pos['y'] + self.size['h'])
            self.t.fillcolor(color)
            self.t.begin_fill()
            self.t.setpos(self.pos['x'] - self.size['w'] / 2, self.pos['y'])
            self.t.setpos(self.pos['x'] + self.size['w'] / 2, self.pos['y'])
            self.t.setpos(self.pos['x'] + self.size['w'] / 2, self.pos['y'] + self.size['h'])
            self.t.setpos(self.pos['x'] - self.size['w'] / 2, self.pos['y'] + self.size['h'])
            self.t.end_fill()
        self.t.setpos(self.pos['x'], self.pos['y'])
        self.t.write(self.text, False, 'center', self.font)

    def _is_in_btn(self, x, y):
        pos = axis_screen_to_turtle(x, y, self.w.canvwidth, self.w.canvheight)
        if (pos['x'] > self.pos['x'] - self.size['w'] / 2 and
            pos['x'] < self.pos['x'] + self.size['w'] / 2 and
            pos['y'] < self.pos['y'] + self.size['h'] and
            pos['y'] > self.pos['y']):
            return True
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
                return True
        return False
    
    def _movein_listener(self, event):
        if int(event.type) != MOTION_EVENT:
            return

        if self._is_move_in(event.x, event.y):
            self._draw('#dddddd')

        if self._is_move_out(event.x, event.y):
            self._draw('#ffffff')

    def _is_click(self, state):
        if state == MOUSE_LEFT_DOWN:
            return True
        else:
            return False

    def _onclick_listener(self, event):
        if int(event.type) != BUTTON_PRESS_EVENT:
            return
        
        if self._is_in_btn(event.x, event.y) and self._is_click(event.state):
            self._callback()
