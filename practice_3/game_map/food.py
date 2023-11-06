from collections.abc import Callable
from random import randint
from turtle import Turtle
from frame import Utils
from .status import Status


class Food:

    def __init__(self, cell_update: Callable[[list[list[int, int, int]]], None]):
        self.status = Status()
        self.t = Turtle()
        Utils.turtle_init(self.t)
        self._cell_update = cell_update
        self._food_init()

    def _update_food(self):
        self.status.refresh_food()
        food_col = self.status.food_col
        food_row = self.status.food_row
        self._cell_update([[food_col, food_row, self.status.FOOD]])

    def _food_init(self):
        self._update_food()
        self.status.collision.register(self.status.GROUP_MAP1,
                                       self.status.NAME_FOOD,
                                       self._update_food)
