from tkinter import *

import pandas
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"
try:
    all_data = pd.read_csv('data/words_to_learn.csv')
except:
    all_data = pd.read_csv('data/french_words.csv')
data = all_data.to_dict(orient='records')
print(data)
next_word = {}


def right_button_function():
    global next_word, flip_timer
    window.after_cancel(flip_timer)
    next_word = random.choice(data)
    canvas.itemconfig(card_title, text='French', fill='black')
    canvas.itemconfig(card_word, text=next_word['French'], fill='black')
    canvas.itemconfig(image_set, image=set_front_img)
    flip_timer = window.after(3000, flit_english)

def flit_english():
    canvas.itemconfig(image_set, image=back_img)
    canvas.itemconfig(card_title, text='English', fill='white')
    canvas.itemconfig(card_word, text=next_word['English'], fill='white')

def know_answer():
    print(next_word)
    data.remove(next_word)
    print(len(data))
    learn_data = pandas.DataFrame(data)
    learn_data.to_csv("data/words_to_learn.csv", index=False)
    right_button_function()

window = Tk()
window.title("Flashy")
flip_timer = window.after(3000, flit_english)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
set_front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
image_set = canvas.create_image(400, 263, image=set_front_img)
card_title = canvas.create_text(400, 150, text='Title', font=('Ariel', 30, 'normal'))
card_word = canvas.create_text(400, 263, text='Word', font=('Ariel', 60, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file='images/right.png')
right_button = Button(image=right_image, command=know_answer)
right_button.grid(column=0, row=1)
wrong_image = PhotoImage(file='images/wrong.png')
wrong_button = Button(image=wrong_image, command=right_button_function)
wrong_button.grid(column=1, row=1)

right_button_function()

window.mainloop()
