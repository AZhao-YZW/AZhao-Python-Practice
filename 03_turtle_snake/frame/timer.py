from collections.abc import Callable
from turtle import Screen


class Timer:

    def __init__(self, func: Callable[[None], None], time: int):
        self.s = Screen()
        self._running = False
        self._func = func
        self._time = time
        self._in_loop = False

    def start(self):
        self._running = True
        self.s.ontimer(self.loop, self._time)

    def stop(self):
        self._running = False

    def is_run(self):
        in_loop = self._in_loop
        self._in_loop = False
        return in_loop

    def set_interval(self, time: int):
        self._time = time

    def loop(self):
        self._in_loop = True
        if self._running:
            self._func()
            self.s.ontimer(self.loop, self._time)
