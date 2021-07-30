import tkinter
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


# ---------------------------- TIMER RESET ------------------------------- # noqa : E501

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="TIMER", fg=GREEN)
    tick_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # noqa : E501


def start_timer():
    global reps
    # work_sec = WORK_MIN * 60
    # short_break_sec = SHORT_BREAK_MIN * 60
    # long_break_sec = LONG_BREAK_MIN * 60

    work_sec = 10
    short_break_sec = 3
    long_break_sec = 5

    reps += 1
    if reps % 2 != 0:
        timer_label.config(text="WORK", fg=GREEN)
        count_down(work_sec)

    elif reps % 8 == 0:
        timer_label.config(text="LONG BREAK", fg=RED)
        count_down(long_break_sec)

    else:
        timer_label.config(text="SHORT BREAK", fg=PINK)
        count_down(short_break_sec)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # noqa : E501


def count_down(count):

    global timer
    global reps

    minutes = int(count / 60)
    seconds = count % 60

    if minutes < 10:
        minutes = f"0{minutes}"

    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:

        timer = window.after(1000, count_down, count - 1)
    else:
        mark = ""
        for i in range(int((reps + 1) / 2)):
            mark += '✔'
        tick_label.config(text=mark)
        if reps == 8:
            reset_timer()
        else:
            start_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.minsize(width=600, height=300)
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = tkinter.Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white",
                                font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

# Timer - Label
timer_label = tkinter.Label(
    text="TIMER", font=(FONT_NAME, 30, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

# Tick - Label
tick_label = tkinter.Label(
    text="", font=(FONT_NAME, 15, "bold"), fg=GREEN, bg=YELLOW)
tick_label.grid(column=1, row=3)

# Start - Button
start_button = tkinter.Button(
    text="Start", command=start_timer, highlightthickness=0)
start_button.grid(column=0, row=2)

# Reset - Button
reset_button = tkinter.Button(
    text="Reset", command=reset_timer, highlightthickness=0)
reset_button.grid(column=2, row=2)

window.mainloop()
