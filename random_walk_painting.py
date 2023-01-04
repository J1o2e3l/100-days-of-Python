import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
screen = Screen()
timmy.shape("turtle")


def random_color():

    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]
timmy.pensize(10)
timmy.speed(0)

for _ in range(500):
    timmy.color(random_color())
    timmy.fd(30)
    timmy.setheading(random.choice(directions))

    
    
screen.exitonclick()
# def draw_shape(sides):
#
#     angle = 360 / sides
#     for _ in range(sides):
#         timmy.fd(100)
#         timmy.rt(angle)
#
#
# for n_side in range(3, 11):
#
#     timmy.color(random.choice(colors))
#     draw_shape(n_side)

# for _ in range(15):
#     timmy.fd(10)
#     timmy.pu()
#     timmy.fd(10)
#     timmy.pd()




# for _ in range(4):
#     timmy.fd(100)
#     timmy.right(90)
























