from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global reps
    reps = 0
    window.after_cancel(timer)
    tick.config(text="")
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label.config(text="Long Break", fg=RED)
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label.config(text="Short Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    minutes = count//60
    if count%60 < 10:
        seconds = f"0{count%60}"
    else:
        seconds = count%60
    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_session = math.floor(reps/2)
        for i in range(work_session):
            mark += "✔"
        tick.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
label.grid(row=0,column=1)

canvas = Canvas(width = 200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)

start_button = Button(text="Start", bg=YELLOW, highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", bg=YELLOW, highlightthickness=0, command=reset)
reset_button.grid(row=2, column=2)

tick = Label(font=(FONT_NAME, 16), fg=GREEN, bg=YELLOW)
tick.grid(row=3,column=1)

window.mainloop()