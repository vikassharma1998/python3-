import pandas
import pandas as pd
from tkinter import *
import random
BACKGROUND_COLOR = "#B1DDC6"
try:
    all_data = pd.read_csv('data/learn_word.csv')
except:
    all_data = pd.read_csv('data/french_words.csv')
data = all_data.to_dict(orient='records')
current_data = {}


def next_word():
    global current_data, flat_time
    window.after_cancel(flat_time)
    current_data = random.choice(data)
    canvas.itemconfig(title_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=current_data['French'], fill='black')
    flat_time = window.after(3000, flat_english)
    canvas.itemconfig(front, image=front_img)


def know_data():
    data.remove(current_data)
    learn_data = pandas.DataFrame(data)
    learn_data.to_csv('data/learn_word.csv', index=False)
    next_word()


def flat_english():
    canvas.itemconfig(title_text, text='English', fill='white')
    canvas.itemconfig(word_text, text=current_data['English'], fill='white')
    canvas.itemconfig(front, image=back_img)


window = Tk()
flat_time = window.after(3000, flat_english)
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_img = PhotoImage(file='images/card_front.png')
back_img = PhotoImage(file='images/card_back.png')
front = canvas.create_image(400, 263, image=front_img)
title_text = canvas.create_text(400, 150, text='Title', font=('Ariel', 30, 'normal'))
word_text = canvas.create_text(400, 263, text='Word', font=('Ariel', 40, 'bold'))
canvas.grid(column=0, row=0, columnspan=2)

# Button
know_button_img = PhotoImage(file='images/right.png')
know_button = Button(image=know_button_img, highlightthickness=0, command=know_data)
know_button.grid(column=1, row=1)
un_know_button_img = PhotoImage(file='images/wrong.png')
un_know_button = Button(image=un_know_button_img, highlightthickness=0, command=next_word)
un_know_button.grid(column=0, row=1)

next_word()
window.mainloop()

