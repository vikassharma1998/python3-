
import turtle
import pandas as pd



screen = turtle.Screen()
screen.title('US State game')
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)
screen.setup(width=800, height=500)
data = pd.read_csv('50_states.csv')
list_of_states = data.state.to_list()
guess_state = []

while len(guess_state) < 50:
    user_input = screen.textinput(title=f'{len(guess_state)}/50 States Correct', prompt="hat's another state's name?").title()
    if user_input == 'Exit':
        missing_state = [state for state in list_of_states if state not in guess_state]
        data_convert_into_csv = pd.DataFrame(missing_state)
        data_convert_into_csv.to_csv('missing_data')
        break
    if user_input in list_of_states:
        guess_state.append(user_input)
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.color('black')
        state_data = data[data['state'] == user_input]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(user_input)
# def fxn(x, y):
#     # set screen color randomly
#     print(x, y)
#     # set screen
#
# # call method on screen click
# turtle.onscreenclick(fxn)
#
# turtle.mainloop()
screen.exitonclick()