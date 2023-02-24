from turtle import Turtle

starting_position = [(0, 0), (-20, 0), (-40, 0)]
moving_distance = 20
up = 90
down = 270
left = 180
right = 0


class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in starting_position:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.goto(position)
        snake.color("white")
        self.snake_body.append(snake)

    def extend(self):
        self.add_segment(self.snake_body[-1].position())

    def move(self):
        for snake in range(len(self.snake_body) - 1, 0, -1):
            new_x = self.snake_body[snake - 1].xcor()
            new_y = self.snake_body[snake - 1].ycor()
            self.snake_body[snake].goto(new_x, new_y)
        self.snake_body[0].forward(moving_distance)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)
