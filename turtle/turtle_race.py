import random
import turtle
from turtle import Turtle, Screen
color = ['red', 'green', 'cyan', 'blue', 'purple', 'pink', 'brown', 'gray']
# timmy = Turtle()
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bat = screen.textinput(title="Make your bet ", prompt=f"Select your turtle color {color}")
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtle = []
for turtle_index in range(0, 6):
    timmy = Turtle(shape="turtle")
    timmy. color(color[turtle_index])
    timmy.penup()
    timmy.goto(x=-220, y=y_positions[turtle_index])
    all_turtle.append(timmy)

if user_bat:
    is_race_on = True

while is_race_on:
    for timmy in all_turtle:
        if timmy.xcor() > 230:
            is_race_on = False
            winning_color = timmy.pencolor()
            if winning_color == user_bat:
                print(f"you've won! The {winning_color} is the winner")
            else:
                print(f"you've lost! The {winning_color} is the winner")
        r_distance = random.randint(1, 10)
        timmy.forward(r_distance)
screen.exitonclick()