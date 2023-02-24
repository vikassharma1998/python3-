from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 1
SHORT_BREAK_MIN = 1
LONG_BREAK_MIN = 20
reps = 0
timers= None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    reps = 0
    window.after_cancel(timers)
    canvas.itemconfig(timer_text, text='00:00')
    timer.config(text='Timer', fg=GREEN)
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long = LONG_BREAK_MIN * 60
    reps += 1
    print(reps)

    if reps % 8 == 0:
        set_timer(long)
        timer.config(text='Break', fg=RED)

    elif reps % 2 == 0:
        set_timer(short_break)
        timer.config(text='Break', fg=PINK)
    else:
        set_timer(work_sec)
        timer.config(text='Work', fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def set_timer(count):
    global timers
    count_min = math.floor(count/60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec =f'0{count_sec}'
    if count_sec == 0:
        count_sec = '00'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_sec}')
    if count > 0:
       timers =  window.after(1000, set_timer, count-1)
    else:
        start()
        checkmark = ''
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            checkmark = '✔'

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(padx=100, pady=100, bg=YELLOW)
window.title("Pomodoro")
timer = Label(text='Timer', bg=YELLOW, fg=GREEN, font=(FONT_NAME, 40, 'normal'))
timer.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=('FONT_NAME', 30, 'normal'))
canvas.grid(column=1, row=1)
start_button = Button(text='Start', width=8, fg=GREEN, command=start)
start_button.grid(column=0, row=3)
reset_button = Button(text='Reset', width=8, fg=RED, command=reset)
reset_button.grid(column=3, row=3)
checkmark = Label(font=(FONT_NAME, 20, 'normal'), bg=YELLOW, fg=GREEN )
checkmark.grid(column=1, row=4)
window.mainloop()
