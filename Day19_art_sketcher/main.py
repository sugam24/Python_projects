from turtle import Turtle, Screen

obj = Turtle()
screen = Screen()


def move_forward():
    obj.forward(10)


def move_backward():
    obj.forward(-10)


def turn_right():
    new_heading = obj.heading() - 10
    obj.setheading(new_heading)


def turn_left():
    new_heading = obj.heading() + 10
    obj.setheading(new_heading)


def clear():
    obj.clear()
    obj.penup()
    obj.home()
    obj.pendown()


screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=turn_right, key="d")
screen.onkey(fun=turn_left, key="a")
screen.onkey(fun=clear, key="c")
screen.exitonclick()
