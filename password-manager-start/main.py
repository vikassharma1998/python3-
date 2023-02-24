from tkinter import *
from tkinter import messagebox

import random
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generate():
    number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    symbol = ['{', '}', '(', ')', '[', ']', '.', ':', ';', '+', '-', '*', '/', '&', '|', '<', '>', '=', '~']
    alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
                'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    random_number = random.randint(2, 4)
    random_symbol = random.randint(2, 4)
    random_alphabet = random.randint(6, 8)
    random_numbers = [random.choice(number) for _ in range(random_number)]
    random_symbols = [random.choice(symbol) for _ in range(random_symbol)]
    random_alphabets = [random.choice(alphabet) for _ in range(random_alphabet)]
    password = random_numbers + random_symbols + random_alphabets
    random.shuffle(password)
    final_password = "".join(map(str,password))
    password_input.insert(0, final_password)
# ---------------------------- SAVE PASSWORD ------------------------------- #


def check_field():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    if len(website) == 0:
        message = messagebox.showwarning(title='Website ', message='Website is required')
    elif len(email) == 0:
        message = messagebox.showwarning(title='Email ', message='Email is required')
    elif len(password) == 0:
        message = messagebox.showwarning(title='Password ', message='Password is required')
    else:
        save_data()


def save_data():
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()
    message = messagebox.askyesno(title='Data Save',
                                  message=F'There are details you Entered: \nEmail:{email} \nWebsite:{website} \npassword:{password}')
    print(message)

    if message:
        with open('passworddata.txt', 'a') as data:
            data.write(f"{website} | {email}  | {password} \n")
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)
            data.close()


# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.config(padx=20, pady=20)
canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(row=0, column=1)
# lable
website_lable = Label(text='Website')
website_lable.grid(row=1, column=0)
email_lable = Label(text='Email/Username')
email_lable.grid(row=2, column=0)
password_lable = Label(text='Password')
password_lable.grid(row=3, column=0)

# input
website_input = Entry(width=50)
website_input.grid(row=1, column=1, columnspan=2)
email_input = Entry(width=50)
email_input.grid(row=2, column=1, columnspan=2)

password_input = Entry(width=30)
password_input.grid(row=3, column=1)

# button
password_generate = Button(text='Generate Password', command=password_generate)
password_generate.grid(row=3, column=2)
add_button = Button(text='Add', width=35, command=check_field)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
