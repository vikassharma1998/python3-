from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color('white')
        self.goto(x=0, y=260)
        self.hideturtle()
        self.update_score_board()

    def update_score_board(self):
        self.write(f"Score: {self.score}", align='center', font=('Arial', 15, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score_board()
    def game_over(self):
        self.goto(x=0, y=0)
        self.write(f"Game Over", align='center', font=('Arial', 15, 'normal'))