from turtle import Screen
from pong import Paddle
from ball import Ball
import time
from scoreboard import Score
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 260 or ball.ycor() < -260:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
    if ball.xcor() > 410:
        ball.reset_position()
        score.l_point()
    if ball.xcor() < -410:
        ball.reset_position()
        score.r_point()

    if score.l_score == 5:
        score.l_winner()
        game_is_on = False

    elif score.r_score == 5:
        score.r_winner()
        game_is_on = False
screen.exitonclick()
