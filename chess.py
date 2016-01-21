import turtle

def one_square(side,filled):
    if filled:
        turtle.begin_fill()
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.left(90)
    turtle.forward(side)
    turtle.end_fill()

side=40
turtle.speed('fastest')

for j in range(8):
    if j % 2==0:
        col_odd=1
    else:
        col_odd=-1
    turtle.penup()
    turtle.goto(0,j*side)
    turtle.pendown()
    for i in range(8):
        if i % 2==0:
            row_odd = 1
        else:
            row_odd = -1
        if (row_odd * col_odd)==1:
            fill_it=True
        else:
            fill_it=False
        one_square(side,fill_it)
        turtle.left(90)
        turtle.forward(side)

turtle.exitonclick()



