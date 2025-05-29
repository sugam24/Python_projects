import turtle as turtle_module
import random
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('Hirst_painting.jpg', 60)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
turtle_module.colormode(255)
color_list = [(1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64),
              (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58),
              (0, 63, 145), (173, 135, 162), (7, 172, 216), (158, 34, 24), (3, 213, 207), (8, 140, 85), (145, 227, 216),
              (122, 193, 148), (102, 220, 229), (221, 178, 216), (253, 197, 0), (80, 135, 179), (122, 169, 190),
              (29, 85, 93), (228, 175, 166), (181, 190, 206), (67, 77, 36), (8, 243, 241)]

obj = turtle_module.Turtle()
obj.speed("fastest")
obj.penup()
obj.hideturtle()
obj.dot(random.choice(color_list))

obj.setheading(225)
obj.forward(300)
obj.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots+1):
    obj.dot(20, random.choice(color_list))
    obj.forward((50))

    if dot_count%10 ==0:
        obj.setheading(90)
        obj.forward(50)
        obj.setheading(180)
        obj.forward(500)
        obj.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
