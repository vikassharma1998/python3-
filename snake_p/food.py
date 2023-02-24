from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color('blue')
        self.refresh()

    def refresh(self):
        x_rand = random.randint(-200, 200)
        y_rand = random.randint(-200, 200)
        self.goto(x=x_rand, y=y_rand)
