import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car:

    def __init__(self):
        self.cars = []

    def create_cars(self):
        random_no = random.randint(1, 6)
        if random_no == 1:
            car = Turtle(shape='square')
            car.penup()
            car.color(random.choice(COLORS))
            car.shapesize(stretch_wid=0.9, stretch_len=2)
            y_new = random.randint(-150, 150)
            car.goto(x=-250, y=y_new)
            self.cars.append(car)

    def move(self):
        for car in self.cars:
            car.forward(5)
