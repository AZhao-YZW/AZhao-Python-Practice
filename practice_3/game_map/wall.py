from turtle import Turtle


class Wall:

    t = Turtle()

    def enable(self):
        self.enable = True

    def disable(self):
        self.enable = False

    def __init__(self, w=500, h=500, enable=True):
        self.w = w
        self.h = h
        self.enable = enable
        self._wall_init()

    def _wall_init(self):
        self._turtle_init()
        self._draw()

    def _turtle_init(self):
        self.t.hideturtle()
        self.t.penup()
        self.t.speed(0)

    def _draw(self):
        self.t.setpos(-self.w / 2, self.h / 2)
        self.t.pendown()
        self.t.setpos(-self.w / 2, -self.h / 2)
        self.t.setpos(self.w / 2, -self.h / 2)
        self.t.setpos(self.w / 2, self.h / 2)
