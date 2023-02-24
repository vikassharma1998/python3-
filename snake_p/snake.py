from turtle import Turtle
set_position = [(0, 0), (-20, 0), (-40, 0)]
right = 0
up = 90
left = 180
down = 270

class Snake(Turtle):

    def __init__(self):
        super().__init__()
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in set_position:
            self.add_body(position)

    def add_body(self, position):
        snake = Turtle(shape='circle')
        snake.penup()
        snake.color('white')
        snake.goto(position)
        self.segment.append(snake)

    def extend(self):
        self.add_body(self.segment[-1].position())

    def move(self):
        for snake in range(len(self.segment)-1, 0, -1):
            new_x = self.segment[snake-1].xcor()
            new_y = self.segment[snake - 1].ycor()
            self.segment[snake].goto(new_x, new_y)
        self.segment[0].forward(20)

    def reset(self):
        for seg in self.segment:
            seg.goto(1000, 1000)
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(180)

