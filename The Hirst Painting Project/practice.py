import turtle
from turtle import Turtle, Screen
import random
tim = Turtle()
tim.shape("turtle")

'''draw a square'''
#
# for _ in range(4):
#     tim.right(90)
#     tim.forward(100)

'''print hero names'''

# import heroes
# print(heroes.gen())

'''print a dashed line'''

# for _ in range(10):
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
#     tim.forward(10)
#

'''draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon and decagon'''

#
# color_list = ["red", "blue", "green", "black"]
#
# for num in range(3, 11):
#     angle = 360/num
#     color = random.choice(color_list)
#     tim.pencolor(color)
#     for _ in range(num):
#         tim.forward(100)
#         tim.right(angle)


'''Draw a random walk'''

#
# import turtle as t
# import random
# t.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
# # color = ["red", "green",'yellow', 'orange', 'red', 'maroon', 'violet', 'magenta', 'purple',
# #          'navy', 'cyan', 'turquoise', 'lightgreen',
# #          'darkgreen', 'chocolate', 'gray']
#
#
# tim.shape('arrow')
# dir_list = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")
#
#
# for _ in range(300):
#     tim.forward(30)
#     tim.setheading(random.choice(dir_list))
#     tim.pencolor(random_color())
#

'''Draw a spirograph'''

#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
#
#
# tim.hideturtle()
#
# size = int(input("enter the gap size : "))
# turtle.colormode(255)
# tim.speed("fastest")
#
#
# for _ in range(round(360/size)):
#     tim.circle(100)
#     tim.setheading(tim.heading()+size)
#     tim.pencolor(random_color())
#
#
#
#
#
#
#
#
# screen = Screen()
# screen.exitonclick()
