import turtle
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.color(black)
    turtle.begin_fill()

    for count in range(4):
        turtle.forward(size)
        turtle.left(90)

    turtle.end_fill()
