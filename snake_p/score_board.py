from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('my_file.txt') as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(x=0, y=220)
        self.update()

    def update(self):
        file = open('my_file.txt', mode='r')
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align='center', font=('Arial', 15, 'normal'))

    def increase(self):
        self.score += 1
        self.update()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            data_file = open('my_file.txt', mode='w')
            data_file.write(f'{self.high_score}')
        self.score = 0
        self.update()
    # def game_over(self):
    #     self.goto(x=0, y=0)
    #     self.write("Game Over", align='center', font=('Arial', 25, 'normal'))
