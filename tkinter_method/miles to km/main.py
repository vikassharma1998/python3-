from tkinter import *

# miles = float(input("Please enter miles:"))
# kilometers = miles * 1.6
# print(kilometers, " Kilometers")
def click_me():
    miles = float(userinput.get())
    kilometers = miles * 1.6
    label = Label(text=kilometers)
    label.place(x=10, y=80)

window = Tk()
window.minsize(width=300, height=100)
label = Label(text='Please enter miles :')
label.place(x=10, y=10)
userinput =Entry(width=20)
userinput.place(x=120, y=12)
button = Button(text="submit", command=click_me)
button.place(x=120, y=40)
window.mainloop()
