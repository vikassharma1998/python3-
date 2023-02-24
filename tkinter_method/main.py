from tkinter import *



window = Tk()
window.title("Robo window")
window.minsize(width=500, height=400)
window.maxsize(width=500, height=400)
label_time = Label(window, text="Right Text")
label_time .pack()

def cick_me():
    output = input.get()
    label_time.config(text= output)
    input.delete(0, END)
button = Button(window, text='Click me', command=cick_me).pack()

input = Entry()
input.pack()

entry = Text(height= 5,width=30)
entry.pack()

window.mainloop()

