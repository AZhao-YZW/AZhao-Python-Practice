from collections.abc import Callable
from turtle import Turtle
from frame import Utils
from .status import Status

class Food:

    def __init__(self, cell_update: Callable[[list[list[int, int, int]]], None]):
        self.status = Status()
        self.t = Turtle()
        Utils.turtle_init(self.t)
        self._cell_update = cell_update

    def _food_init(self):
        pass