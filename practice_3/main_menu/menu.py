from collections.abc import Callable
from turtle import Turtle
from turtle import Screen
from frame import MotionEvent
from frame import GameWindow
from frame import Utils
from component import Button


class Menu:
    '''
    game_start: 开始游戏回调函数;
    game_exit: 退出游戏回调函数
    '''
    s = Screen()
    motion_event = MotionEvent()
    w = GameWindow()
    mouse = Turtle()
    t = Turtle()

    def __init__(self, game_start, game_exit):
        self._game_start = game_start
        self._game_exit = game_exit
        Utils.turtle_init(self.mouse)
        Utils.turtle_init(self.t)
        self._menu_init()

    def _menu_init(self):
        self.t.setpos(0, 200)
        self.t.write('贪吃蛇', False, 'center', ('Arial', 52, 'normal'))
        self._button_init()
        self._mouse_init()

    def _button_init(self):
        self.btn_start = Button('开始游戏',
                                0, 0, 200, 50,
                                ('Arial', 24, 'normal'))
        self.btn_start.onclick(self._menu_start)
        self.btn_exit = Button('退出游戏',
                               0, -100, 200, 50,
                               ('Arial', 24, 'normal'))
        self.btn_exit.onclick(self._menu_exit)

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

    def _menu_exit(self):
        self.btn_start.ondestroy()
        self.btn_exit.ondestroy()
        self.motion_event.unbind(self._mouse_move_listener)
        self.s.clearscreen()
        self._game_exit()

    def _menu_start(self):
        self.btn_start.ondestroy()
        self.btn_exit.ondestroy()
        self.motion_event.unbind(self._mouse_move_listener)
        self.s.clearscreen()
        self._game_start()
