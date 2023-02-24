from turtle import Turtle
import random

y_range = [20,30,40,50,60,70,80,90,100]


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color('white')
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
        # for i in range(10, 350):
        #     self.goto(x=i+10, y=random.choice(y_range))

    def move(self):
        x_new = self.xcor() + self.x_move
        y_new = self.ycor() + self.y_move
        self.goto(x_new, y_new)

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    def bounce_y(self):
        self.y_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()