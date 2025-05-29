import turtle
from turtle import Turtle, Screen
import random

obj = Turtle()
obj.shape("arrow")
obj.color("black")

direction = [0, 90, 180, 270]

# obj.pensize(15)
obj.speed("fastest")
turtle.colormode(255)


def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


# for _ in range(200):
#     obj.color(random_colour())
#     obj.forward(30)
#     obj.setheading(random.choice(direction))


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        obj.color(random_colour())
        obj.circle(100)
        obj.setheading(obj.heading()+size_of_gap)


draw_spirograph(5)
screen = Screen()
screen.exitonclick()
