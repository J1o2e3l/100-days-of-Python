# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('hirst.png', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     color = (r, g, b)
#     rgb_colors.append(color)
#
# print(rgb_colors)

import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed(0)
tim.pu()
tim.ht()

color_list = [(242, 243, 245), (230, 228, 224), (236, 241, 238), (241, 236, 240), (198, 159, 116), (70, 92, 129), (147, 85, 53),
 (218, 210, 116), (138, 160, 191), (178, 160, 38), (184, 146, 164), (28, 32, 46), (58, 34, 23), (120, 70, 93),
 (139, 175, 154), (77, 115, 79), (143, 25, 16), (186, 97, 82), (61, 31, 42), (121, 27, 41), (45, 58, 94),
 (177, 96, 114), (102, 119, 170), (34, 52, 45), (100, 160, 85), (214, 175, 192), (216, 181, 173), (160, 209, 191),
 (67, 86, 23), (219, 206, 8)]


tim.setheading(225)
tim.fd(300)
tim.setheading(0)
dots = 100

for dot_count in range(1, dots+1):

    tim.dot(20, random.choice(color_list))
    tim.fd(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
