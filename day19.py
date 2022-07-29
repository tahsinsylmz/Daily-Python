from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def w():
    tim.forward(10)


def s():
    tim.backward(10)


def a():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def d():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def c():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(a, "a")
screen.onkey(d, "d")
screen.onkey(w, "w")
screen.onkey(s, "s")
screen.onkey(c, "c")


screen.exitonclick()

