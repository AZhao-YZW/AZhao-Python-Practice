from abc import ABCMeta, abstractmethod
from turtle import Screen


class Event:

    __meta_class__ = ABCMeta
    listener_list = []
    s = Screen()

    def __init__(self):
        print('Event init')

    def trigger_listener(self, event):
        for listener in self.listener_list:
            listener(event)
            # print(event, event.type)

    def bind(self, func):
        self.listener_list.append(func)

    def unbind(self, func):
        self.listener_list.remove(func)


class _MotionEvent(Event):

    _motion_event = None

    def __init__(self):
        super().__init__()
        self.s.getcanvas().bind('<Motion>', self.trigger_listener)
        print('_MotionEvent init')

class _ButtonPressEvent(Event):

    _btn_press_event = None

    def __init__(self):
        super().__init__()
        self.s.getcanvas().bind('<Button-1>', self.trigger_listener)
        print('_ButtonPressEvent init')

# 每种事件类均为单例
def MotionEvent():
    if _MotionEvent._motion_event is None:
        _MotionEvent._motion_event = _MotionEvent()
    return _MotionEvent._motion_event

def ButtonPressEvent():
    if _ButtonPressEvent._btn_press_event is None:
        _ButtonPressEvent._btn_press_event = _ButtonPressEvent()
    return _ButtonPressEvent._btn_press_event