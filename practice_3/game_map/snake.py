from turtle import Turtle
from frame import Utils
from .status import Status

class Snake:

    def __init__(self):
        self.status = Status()
        self.t = Turtle()
        Utils.turtle_init(self.t)
        self._snake_init()

    def _snake_init(self):
        pass