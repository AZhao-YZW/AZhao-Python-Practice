from abc import ABCMeta, abstractmethod
from turtle import Screen


class Event:

    __meta_class__ = ABCMeta
    s = Screen()

    def __init__(self):
        self.listener_list = []

    def _trigger_listener(self, event):
        for listener in self.listener_list:
            listener(event)

    def bind(self, func):
        self.listener_list.append(func)

    def unbind(self, func):
        self.listener_list.remove(func)


class _MotionEvent(Event):

    _event = None

    def __init__(self):
        super().__init__()
        self.s.getcanvas().bind('<Motion>', self._trigger_listener)


class _MouseLPressEvent(Event):

    _event = None

    def __init__(self):
        super().__init__()
        self.s.getcanvas().bind('<Button-1>', self._trigger_listener)


# 每种事件类均为单例


def MotionEvent():
    if _MotionEvent._event is None:
        _MotionEvent._event = _MotionEvent()
    return _MotionEvent._event


def MouseLPressEvent():
    if _MouseLPressEvent._event is None:
        _MouseLPressEvent._event = _MouseLPressEvent()
    return _MouseLPressEvent._event
