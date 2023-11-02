from collections.abc import Callable
from turtle import Turtle
from turtle import Screen
from frame import MotionEvent
from frame import GameWindow
from frame import Utils
from component import Button, Text, Mouse


class Menu:
    '''
    game_start: 开始游戏回调函数;
    game_exit: 退出游戏回调函数
    '''
    s = Screen()
    motion_event = MotionEvent()
    w = GameWindow()
    mouse = Mouse()
    t = Turtle()

    def __init__(self, game_start, game_exit):
        self._game_start = game_start
        self._game_exit = game_exit
        Utils.turtle_init(self.t)
        self._menu_init()

    def _menu_init(self):
        self.text_title = Text('贪吃蛇',
                               0, 200, 'center',
                               ('Arial', 52, 'normal'))
        self.btn_start = Button('开始游戏',
                                0, 0, 200, 50, 'center',
                                ('Arial', 24, 'normal'))
        self.btn_start.onclick(self._menu_start)
        self.btn_exit = Button('退出游戏',
                               0, -100, 200, 50, 'center',
                               ('Arial', 24, 'normal'))
        self.btn_exit.onclick(self._menu_exit)

    def _menu_destroy(self):
        self.btn_start.ondestroy()
        self.btn_exit.ondestroy()
        self.w.clear_window()

    def _menu_exit(self):
        self._menu_destroy()
        self._game_exit()

    def _menu_start(self):
        self._menu_destroy()
        self._game_start()
