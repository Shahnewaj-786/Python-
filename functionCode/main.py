import turtle

turtle.shape("turtle")
turtle.speed(9)
turtle.color("green")


def draw_squr(side_len):
    for i in range(4):
        turtle.forward(side_len)
        turtle.left(90)


counter = 0

while counter < 90:
    draw_squr(100)
    turtle.right(4)
    counter += 1

turtle.exitonclick()
