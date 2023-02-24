# from turtle import Turtle, Screen
# import random
# color = ['red', 'green', 'cyan', 'blue', 'purple', 'pink', 'brown', 'gray']
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# x = 3
# for i in range(6):
#     z = 360/x
#     print(z)
#     print(x)
#     for _ in range(x):
#          timmy.lt(z)
#          timmy.forward(100)
#     x+=1
#     timmy.color(random.choice(color))
#     print(x)
# angle =[20,30,40,50,60,70,80,90,100]
# for i in range(10):
#     timmy.color(random.choice(color))
#     timmy.forward(20)
#     timmy.lt(random.choice(angle))
#     timmy.forward(20)













# for i in range(15):
#     timmy.penup()
#     timmy.forward(20)
#     # timmy.pendown()
#     timmy.dot(10)
# def drow(size_of_graph):
#     for i in range(int(366/size_of_graph)):
#         timmy.circle(100)
#         timmy.speed(100)
#         timmy.rt(size_of_graph)
#         timmy.color(random.choice(color))
#     # timmy.pendown()
# drow(5)


############################## final project #############
# timmy.rt(145)
# timmy.color('white')
# timmy.forward(350)
# timmy.lt(145)
# timmy.color('red')
# def step():
#     for i in range(28):
#         timmy.dot(10)
#         timmy.color(random.choice(color))
#         timmy.penup()
#         timmy.forward(20)
#         timmy.pendown()
#
# def right():
#     timmy.dot(10)
#     timmy.lt(90)
#     timmy.penup()
#     timmy.forward(20)
#     timmy.lt(90)
#     step()
# def left():
#     timmy.dot(10)
#     timmy.rt(90)
#     timmy.penup()
#     timmy.forward(20)
#     timmy.rt(90)
#     step()
# step()
# for i in range(10):
#     right()
#     left()

# my_screen = Screen()
# my_screen.exitonclick()


# from prettytable  import PrettyTable
#
# x = PrettyTable()
# x.add_column("City", ['mumbji', 'Delhi', 'banglore'])
# x.add_column("PinCode", ['123456', '987891', '654345'])
# print(x)


from turtle import Turtle, Screen
import random
color = ['red', 'green', 'cyan', 'blue', 'purple', 'pink', 'brown', 'gray']
timmy = Turtle()
print(timmy)
timmy.shape("turtle")
my_screen = Screen()

def move_forword():
    timmy.forward(10)
def move_backward():
    timmy.backward(10)
def move_right():
    new_right = timmy.heading() - 10
    timmy.setheading(new_right)
def move_left():
    new_right = timmy.heading() + 10
    timmy.setheading(new_right)
def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()
my_screen.listen()
my_screen.onkey(key='w', fun=move_forword)
my_screen.onkey(key='s', fun=move_backward)
my_screen.onkey(key='d', fun=move_right)
my_screen.onkey(key='a', fun=move_left)
my_screen.onkey(key='c', fun=clear)
my_screen.exitonclick()