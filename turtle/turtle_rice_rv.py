from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
color = ['red', 'orange', 'cyan', 'green', 'blue', 'yellow']
turtle_gap = [-70, -40, -10, 20, 50, 80]
all_turtle = []
game_is_on = False
user_bat = screen.textinput(title='Turtle Bat Game', prompt=f'Select your color {color}')

for i in range(0, 6):
    timmy = Turtle(shape="turtle")
    timmy.penup()
    timmy.color(color[i])
    timmy.goto(x=-230, y=turtle_gap[i])
    all_turtle.append(timmy)
if user_bat:
    game_is_on = True

while game_is_on:
    for timmy in all_turtle:
        if timmy.xcor() > 230:
            game_is_on = False
            winning_color = timmy.pencolor()
            if winning_color == user_bat:
                print(f"you've win! The {winning_color} is the winner")
            else:
                print(f"you've lose! The {winning_color} is the winner")
        timmy.forward(random.randint(0, 10))
screen.exitonclick()

