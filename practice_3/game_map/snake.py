from collections.abc import Callable
from turtle import Turtle
from frame import Utils
from frame import KeyPressEvent
from frame import Timer
from .status import Status


class Snake:

    def ondestroy(self):
        self.keypress_event.unbind(self._snake_move_listener)
        self.timer.stop()

    def __init__(self, cell_update: Callable[[list[list[int, int, int]]], None]):
        self.status = Status()
        print(self.status)
        self.keypress_event = KeyPressEvent()
        self.timer = Timer(self._snake_move,
                           int(1000 / self.status.snake_speed))
        self.t = Turtle()
        Utils.turtle_init(self.t)
        self._cell_update = cell_update
        self._snake_init()

    def _snake_init(self):
        head_col = self.status.snake_head_col
        head_row = self.status.snake_head_row
        for i in range(self.status.snake_len):
            self.status.snake_list.append(
                [head_col - i, head_row, self.status.SNAKE])
            self._cell_update(self.status.snake_list)

        self.keypress_event.bind(self._snake_move_listener)
        self.timer.start()

    def _snake_move(self):
        dir = self.status.snake_dir
        hor = 0
        ver = 0
        if dir == 'l':
            hor = -1
        elif dir == 'u':
            ver = 1
        elif dir == 'd':
            ver = -1
        elif dir == 'r':
            hor = 1

        self.status.snake_head_col += hor
        self.status.snake_head_row -= ver
        snake_list = self.status.snake_list
        snake_list.insert(0, [self.status.snake_head_col,
                              self.status.snake_head_row,
                              self.status.SNAKE])
        snake_list[len(snake_list) - 1][2] = self.status.BLANK
        # 仅需更新头尾格子
        cell_list = [snake_list[0], snake_list[len(snake_list) - 1]]
        snake_list.pop()
        self._cell_update(cell_list)

    def _snake_move_listener(self, event):
        key = event.char
        if key not in ('a', 'w', 's', 'd',
                       'A', 'W', 'S', 'D'):
            return

        cur_dir = self.status.snake_dir
        if key in ('a', 'A'):
            self.status.snake_dir = 'l' if cur_dir != 'r' else cur_dir
        elif key in ('w', 'W'):
            self.status.snake_dir = 'u' if cur_dir != 'd' else cur_dir
        elif key in ('s', 'S'):
            self.status.snake_dir = 'd' if cur_dir != 'u' else cur_dir
        elif key in ('d', 'D'):
            self.status.snake_dir = 'r' if cur_dir != 'l' else cur_dir
