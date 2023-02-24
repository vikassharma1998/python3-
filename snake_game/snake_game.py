from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Score
screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)
game_on = True
snake = Snake()
food = Food()
score = Score()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.game_over()
        game_on = False
    for segment in snake.snake_body:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            score.game_over()
            game_on = False

screen.exitonclick()
