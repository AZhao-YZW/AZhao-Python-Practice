from collections.abc import Callable
from turtle import Screen


class Timer:

    def __init__(self, func: Callable[[None], None], time: int):
        self.s = Screen()
        self._running = False
        self._func = func
        self._time = time

    def start(self):
        self._running = True
        self.s.ontimer(self.loop, self._time)

    def stop(self):
        self._running = False

    def interval(self, time: int):
        self._time = time

    def loop(self):
        if self._running:
            self._func()
            self.s.ontimer(self.loop, self._time)
