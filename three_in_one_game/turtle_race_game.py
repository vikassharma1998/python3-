from turtle import Turtle, Screen
import random

screen = Screen()
color = ['red', 'blue', 'cyan', 'yellow', 'gray', 'pink']
userinput = screen.textinput(title='Welcome to Turtle Game', prompt=f'Select your Turtle color {color}')
screen.setup(width=500, height=400)
position_set = [-70, -40, -10, 20, 50, 80, 110]
turtle_list = []
for position in range(0, 6):
    turtle = Turtle(shape='turtle')
    turtle.penup()
    turtle.color(color[position])
    turtle.goto(x=-230, y=position_set[position])
    turtle_list.append(turtle)

if userinput:
    game_is_on = True


def check_winner():
    winner = Turtle()
    winner.hideturtle()
    if winner == userinput:
        winner.write(f"you've won! The {winner} is the winner ", align='center', font=('courier', 15, 'normal'))
    else:
        winner.write(f"you.ve lose! The {winner} is the winner", align='center', font=('courier', 15, 'normal'))


while game_is_on:
    for timmy in turtle_list:
        if timmy.xcor() > 230:
            game_is_on = False
            winner = timmy.pencolor()
            check_winner()
        timmy.forward(random.randint(0, 10))
screen.exitonclick()
