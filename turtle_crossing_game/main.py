from turtle import Screen
from car import Car
from player import Player
from scoreboard import Score
import time
screen = Screen()

screen.bgcolor('white')
screen.setup(width=500, height=400)
screen.tracer(0)

car = Car()
player = Player()
score = Score()

screen.listen()
screen.onkey(player.up, 'Up')
screen.onkey(player.down, 'Down')

game_is_on = True
while game_is_on:
    car.create_cars()
    screen.update()
    time.sleep(score.speed)
    car.move()

    for c in car.cars:
        if c.distance(player) < 30:
            game_is_on = False
            score.game_over()

    if player.ycor() > 170:
        score.increase_score()
        player.refresh()

screen.exitonclick()
