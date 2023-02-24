from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('blue')
        self.goto(x=0, y=-180)
        self.lt(90)

    def up(self):
        self.forward(10)

    def down(self):
        self.backward(10)

    def refresh(self):
        self.goto(x=0, y=-180)
