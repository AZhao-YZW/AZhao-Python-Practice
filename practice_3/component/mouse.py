from turtle import Turtle
from frame import Utils
from frame import MotionEvent
from frame import GameWindow


class _Mouse:

    _mouse = None
    motion_event = MotionEvent()
    w = GameWindow()
    mouse = Turtle()

    def mouse_destroy(self):
        '''在需要隐藏鼠标时调用'''
        self.motion_event.unbind(self._mouse_move_listener)
        self.mouse.hideturtle()
        self._mouse = None

    def __init__(self):
        Utils.turtle_init(self.mouse)
        self._mouse_init()

    def _mouse_init(self):
        self.mouse.color('red')
        self.mouse.shape('turtle')
        self.mouse.shapesize(1.5)
        self.mouse.left(120)
        self.motion_event.bind(self._mouse_move_listener)
        self.mouse.showturtle()

    def _mouse_move_listener(self, event):
        x, y = Utils.axis_adapter(event.x, event.y,
                                  self.w.canvwidth, self.w.canvheight)
        self.mouse.setpos(x, y)


def Mouse():
    if _Mouse._mouse is None:
        _Mouse._mouse = _Mouse()
    return _Mouse._mouse
