import turtle
from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

is_race_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Choose the colour of your turtle:")
colors = ["red", "orange", "yellow", "green", "blue", "indigo"]
a = 0

all_turtles = []
for index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[index])
    new_turtle.goto(x=-230, y=-125 + a)
    a += 50
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"Congratulations!!! {winning_color} turtle has won the race.")
            else:
                print(f"Sorry!!! You lost. {winning_color} turtle has won the race.")
        random_distance = random.randint(1,10)
        turtle.forward(random_distance)

screen.exitonclick()
