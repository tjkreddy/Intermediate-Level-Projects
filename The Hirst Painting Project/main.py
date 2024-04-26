# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpeg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
import turtle
import random

from turtle import Turtle
tim = Turtle()
tim.shape('arrow')
turtle.colormode(255)
color_list = [(137, 162, 190), (82, 97, 136), (154, 78, 64), (139, 72, 91), (189, 138, 158), (137, 174, 148),
              (80, 117, 94), (221, 200, 118), (209, 224, 216), (201, 212, 223), (148, 153, 76), (187, 102, 79),
              (105, 119, 168), (176, 97, 120), (225, 212, 219), (100, 143, 118), (167, 204, 185), (217, 174, 192),
              (105, 46, 49), (63, 47, 45), (105, 47, 45), (179, 189, 213), (58, 55, 89), (219, 179, 170), (68, 45, 51),
              (44, 53, 75), (91, 141, 155), (170, 199, 208)]


tim.hideturtle()

tim.penup()
tim.setheading(210)
tim.forward(600)

tim.setheading(0)

for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.setheading(90)
    tim.forward(50)
    tim.setheading(180)
    tim.forward(500)
    tim.setheading(0)


turtle.Screen()
turtle.exitonclick()
