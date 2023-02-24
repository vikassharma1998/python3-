from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(x=-180, y=160)
        self.hideturtle()
        self.update()
        self.speed = 0.1

    def update(self):
        self.clear()
        self.write(f"Level: {self.level}", align='center', font=('Arial', 20, 'normal'))

    def increase_score(self):
        self.level += 1
        self.update()
        self.speed *= 0.9

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("Game Over", align='center', font=('Arial', 20, 'normal'))
