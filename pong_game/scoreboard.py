from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.goto(x=-100, y=200)
        self.write(self.l_score, align='center', font=('courier', 80, 'normal'))
        self.goto(x=100, y=200)
        self.write(self.r_score, align='center', font=('courier', 80, 'normal'))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update()

    def l_winner(self):
        self.goto(x=0, y=0)
        self.write("Left Player is winner", align='center', font=('courier', 30, 'normal'))

    def r_winner(self):
        self.goto(x=0, y=0)
        self.write("Right Player is winner", align='center', font=('courier', 80, 'normal'))
