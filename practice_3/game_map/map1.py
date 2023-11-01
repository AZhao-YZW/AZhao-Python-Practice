from turtle import Turtle
from turtle import Screen
from .wall import Wall
from .food import Food
from .snake import Snake
from frame import MotionEvent
from frame import GameWindow
from frame import Utils
from component import Button, Text, Mouse


class _Map1:

    _map1 = None

    def __init__(self, return_menu):
        self.mouse = Mouse()
        self.t = Turtle()
        self.s = Screen()
        self.w = GameWindow()
        self.motion_event = MotionEvent()
        self.wall = Wall()
        self.food = Food()
        self.snake = Snake()

        self._return_menu = return_menu
        Utils.turtle_init(self.t)
        self._map1_init()

    def _map1_init(self):
        self.text_title = Text('贪吃蛇',
                               0, 360, 'center',
                               ('Arial', 24, 'normal'))
        self.btn_exit = Button('返回主菜单',
                               -400, 370, 140, 30, 'center',
                               ('Arial', 16, 'normal'))
        self.btn_exit.onclick(self._map1_exit)

    def _map1_destroy(self):
        self.btn_exit.ondestroy()
        self.w.clear_window()

    def _map1_exit(self):
        self._map1_destroy()
        self._return_menu()
        self._map1 = None


def Map1(return_menu):
    if _Map1._map1 is None:
        _Map1._map1 = _Map1(return_menu)
    return _Map1._map1
