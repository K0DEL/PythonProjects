import tkinter
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

try:
    data = pandas.read_csv("./data/to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")

to_learn = data.to_dict(orient="records")
word_dict = {}

# Word Change


def get_word():
    global word_dict, flip_timer
    window.after_cancel(flip_timer)

    word_dict = random.choice(to_learn)

    bg_canvas.itemconfig(card_image, image=foreground_img)
    bg_canvas.itemconfig(
        card_word, text=word_dict["French"], fill="black")
    bg_canvas.itemconfig(card_title, text="french", fill="black")
    flip_timer = window.after(3000, flip_card)

# Flip Card


def flip_card():
    global word_dict

    bg_canvas.itemconfig(card_image, image=background_img)
    bg_canvas.itemconfig(
        card_word, text=word_dict["English"], fill="white")
    bg_canvas.itemconfig(card_title, text="English", fill="white")


# is known
def is_known():
    to_learn.remove(word_dict)
    data = pandas.DataFrame(to_learn)
    data.to_csv("./data/to_learn.csv", index=False)
    get_word()


window = tkinter.Tk()
window.title("Flash Card")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Background Canvas
bg_canvas = tkinter.Canvas(width=800, height=526,
                           highlightthickness=0, bg=BACKGROUND_COLOR)
foreground_img = tkinter.PhotoImage(file="./images/card_front.png")
background_img = tkinter.PhotoImage(file="./images/card_back.png")

card_image = bg_canvas.create_image(400, 263, image=foreground_img)
card_title = bg_canvas.create_text(
    400, 150, text="", font=("Arial", 40, "italic"))
card_word = bg_canvas.create_text(
    400, 263, text="", font=("Arial", 60, "bold"))
bg_canvas.grid(column=0, row=0, columnspan=5)
flip_timer = window.after(3000, flip_card)
get_word()

# Right Button
right_img = tkinter.PhotoImage(file="./images/right.png")
right_button = tkinter.Button(
    image=right_img, bg=BACKGROUND_COLOR,
    highlightthickness=0,
    command=is_known
)
right_button.grid(column=1, row=1)

# Wrong Button
wrong_img = tkinter.PhotoImage(file="./images/wrong.png")
wrong_button = tkinter.Button(
    image=wrong_img, bg=BACKGROUND_COLOR,
    highlightthickness=0,
    command=get_word
)
wrong_button.grid(column=3, row=1)


window.mainloop()
