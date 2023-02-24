from turtle import Screen
from snake import Snake
import time
from food import Food
from score_board import Score
screen = Screen()
screen.bgcolor('black')
screen.tracer(0)
snake = Snake()
food = Food()
score = Score()
screen.listen()

screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase()
    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 260 or snake.head.ycor() < -260:
        score.reset()
        snake.reset()

    for segment in snake.segment:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()




screen.exitonclick()
