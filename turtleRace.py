import turtle
from turtle import Turtle, Screen
import random
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Place your bet", prompt="Who will win? Enter Color red/green/blue/orange/purple: ")
colors = ["purple", "orange", "blue", "red", "green", "yellow"]
y_pos = [-70, -40, -10, 20, 50, 80]
turtles=[]

for index in range(0, 5):
    new_turtle = Turtle("turtle")
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(x=-240, y=y_pos[index])
    turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in turtles:

        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You won! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")

        distance = random.randint(0, 10)
        turtle.forward(distance)




screen.exitonclick()
