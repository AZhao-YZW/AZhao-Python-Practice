from turtle import Turtle


class Utils:

    def turtle_init(t: Turtle):
        t.hideturtle()
        t.penup()
        t.speed(0)

    def axis_adapter(sx: float, sy: float,
                     canvwidth: int, canvheight: int) -> tuple[float, float]:
        '''screen (x, y) cast to turtle (x, y)'''
        tx = sx - canvwidth / 2
        ty = -(sy - canvheight / 2)
        return tx, ty
