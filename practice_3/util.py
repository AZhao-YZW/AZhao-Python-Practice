def axis_screen_to_turtle(sx, sy, canvwidth, canvheight):
    tx = sx - canvwidth / 2
    ty = -(sy - canvheight / 2)
    return {'x': tx, 'y': ty}
