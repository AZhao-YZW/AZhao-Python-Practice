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

        self.dir_lock = False
        self.next_next_dir = None
        self.status.collision.register(self.status.GROUP_MAP1,
                                       self.status.NAME_SNAKE,
                                       None)
        self.keypress_event.bind(self._snake_move_listener)
        self.timer.start()

    def _is_collision_wall(self, head_col, head_row):
        if (head_col >= self.status.CELL_COLUMN_NUM or head_col < 0 or
                head_row >= self.status.CELL_ROW_NUM or head_row < 0):
            return True
        else:
            return False

    def _is_collision_self(self, head_col, head_row):
        if self.status.map1[head_row][head_col] == self.status.SNAKE:
            return True
        else:
            return False

    def _is_collision_food(self, head_col, head_row):
        if self.status.map1[head_row][head_col] == self.status.FOOD:
            return True
        else:
            return False

    def _change_dir(self, cur_dir, key):
        if key in ('a', 'A'):
            return 'l' if cur_dir != 'r' else cur_dir
        elif key in ('w', 'W'):
            return 'u' if cur_dir != 'd' else cur_dir
        elif key in ('s', 'S'):
            return 'd' if cur_dir != 'u' else cur_dir
        elif key in ('d', 'D'):
            return 'r' if cur_dir != 'l' else cur_dir

    def _update_dir(self, key):
        if self.dir_lock:
            self.next_next_dir = self._change_dir(self.status.snake_dir, key)
            return

        next_dir = self._change_dir(self.status.snake_dir, key)
        if next_dir == self.status.snake_dir:
            return
        self.status.snake_dir = next_dir

        self.dir_lock = True

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

        head_col = self.status.snake_head_col + hor
        head_row = self.status.snake_head_row - ver
        if self._is_collision_wall(head_col, head_row):
            print('pang wall!!!!!!!!!!!!!!')
            self.dir_lock = False
            return
        if self._is_collision_self(head_col, head_row):
            print('pang self!!!!!!!!!!!!!!')
            self.dir_lock = False
            return

        self.status.snake_head_col += hor
        self.status.snake_head_row -= ver
        snake_list = self.status.snake_list
        snake_list.insert(0, [self.status.snake_head_col,
                              self.status.snake_head_row,
                              self.status.SNAKE])
        snake_list[len(snake_list) - 1][2] = self.status.BLANK
        # 仅需更新头尾格子
        cell_list = [snake_list[0], snake_list[len(snake_list) - 1]]

        if self._is_collision_food(head_col, head_row):
            print('have food!!!!!!!!!!!!!!')
            self.status.collision.notify(self.status.GROUP_MAP1,
                                         self.status.NAME_FOOD)
        else:
            snake_list.pop()

        self._cell_update(cell_list)

        if self.next_next_dir is not None:
            self.status.snake_dir = self.next_next_dir
            print('########## NONONO')
            self.next_next_dir = None
            self._snake_move()

        self.dir_lock = False

    def _snake_move_listener(self, event):
        key = event.char
        if key not in ('a', 'w', 's', 'd',
                       'A', 'W', 'S', 'D'):
            return

        self._update_dir(key)
