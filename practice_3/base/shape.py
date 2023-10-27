from turtle import Turtle


class Shape:
    '''基本形状使用Shape类来画，减少Turtle对象的使用数量'''
    t = Turtle()

    def __init__(self):
        self._turtle_init()

    def _turtle_init(self):
        self.t.hideturtle()
        self.t.penup()
        self.t.speed(0)

    def rect(self, x, y, w, h, anchor='top-left'):
        if anchor in ('top-left', 'tl'):
            tl = (x, y)
        elif anchor in ('top-right', 'tr'):
            tl = (x - w, y)
        elif anchor in ('bottom-left', 'bl'):
            tl = (x, y + h)
        elif anchor in ('bottom-right', 'br'):
            tl = (x - w, y + h)
        elif anchor in ('center'):
            tl = (x - w, y + h)
        else:
            raise ValueError('anchor is wrong')

        bl = (tl[0], tl[1] - h)
        br = (tl[0] + w, tl[1] - h)
        tr = (tl[0] + w, tl[1])

        self.t.penup()
        self.t.setpos(tl)
        self.t.pendown()
        self.t.setpos(bl)
        self.t.setpos(br)
        self.t.setpos(tr)
        self.t.setpos(tl)
        self.t.penup()
