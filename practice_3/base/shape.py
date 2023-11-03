from turtle import Turtle


class Shape:
    '''基本形状使用Shape类来画'''

    def line(t:Turtle, x, y, len, orient='horizontal',
             bordercolor='#000000', borderwidth=1):
        start = (x, y)
        if orient in ('horizontal', 'h'):
            end = (x + len, y)
        elif orient in ('vertical', 'v'):
            end = (x, y - len)
        else:
            raise ValueError('orient is wrong')
        
        t.penup()
        t.setpos(start)
        t.pendown()
        t.color(bordercolor)
        t.pensize(borderwidth)
        t.setpos(end)
        t.penup()


    def rect(t: Turtle, x, y, w, h, anchor='top-left',
             border=True, bordercolor='#000000', borderwidth=1,
             fill=False, fillcolor='#ffffff'):
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

        t.penup()
        t.setpos(tl)
        if border:
            t.pendown()
            t.color(bordercolor)
            t.pensize(borderwidth)
        if fill:
            t.fillcolor(fillcolor)
            t.begin_fill()
        t.setpos(bl)
        t.setpos(br)
        t.setpos(tr)
        t.setpos(tl)
        if fill:
            t.end_fill()
        t.penup()
