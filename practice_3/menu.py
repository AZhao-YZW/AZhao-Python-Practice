from turtle import Turtle
from turtle import Screen
from event import MotionEvent
from util import *
from game_window import GameWindow
from button import Button


class Menu:

    s = Screen()
    motion_event = MotionEvent()
    mouse = Turtle()
    t = Turtle()
    w = GameWindow()
    btn_start: Button
    btn_exit: Button
    _game_start = None
    _game_exit = None

    def __init__(self, game_start, game_exit):
        self._game_start = game_start
        self._game_exit = game_exit
        self.menu_init()

    def menu_init(self):
        self.turtle_init()
        self.t.setpos(0, 200)
        self.t.write('贪吃蛇', False, 'center', ('Arial', 52, 'normal'))
        self.button_init()
        self.mouse_init()

    def turtle_init(self):
        self.t.hideturtle()
        self.t.penup()
        self.t.speed(0)

    def button_init(self):
        self.btn_start = Button(self.mouse,
                                '开始游戏',
                                0, 0, 200, 50,
                                ('Arial', 24, 'normal'))
        self.btn_start.onclick(self.game_start)
        self.btn_exit = Button(self.mouse,
                                '退出游戏',
                                0, -100, 200, 50,
                                ('Arial', 24, 'normal'))
        self.btn_exit.onclick(self.menu_exit)

    def mouse_init(self):
        self.mouse.hideturtle()
        self.mouse.penup()
        self.mouse.color('red')
        self.mouse.speed(0)
        self.mouse.shape('turtle')
        self.mouse.shapesize(1.5)
        self.mouse.left(120)
        self.motion_event.bind(self.mouse_move_listener)
        self.mouse.showturtle()

    def mouse_move_listener(self, event):
        pos = axis_screen_to_turtle(event.x, event.y,
                                    self.w.canvwidth, self.w.canvheight)
        self.mouse.setpos(pos['x'], pos['y'])

    def menu_exit(self):
        self.btn_start.ondestroy()
        self.btn_exit.ondestroy()
        self.motion_event.unbind(self.mouse_move_listener)
        self.s.clearscreen()
        self._game_exit()

    def game_start(self):
        self.btn_start.ondestroy()
        self.btn_exit.ondestroy()
        self.s.clearscreen()
        self._game_start()
