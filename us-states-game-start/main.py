import turtle
import pandas

ALIGNMENT = "center"
FONT = ("Courier", 8, "normal")

screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = turtle.Turtle()
writer.hideturtle()
writer.penup()

guessed_states = []
data = pandas.read_csv("50_states.csv")

while len(guessed_states) != 50:

    answer_state = screen.textinput(
        title=f"{len(guessed_states)} / 50. Guess The State",
        prompt="What's the another State's name"
    ).title()

    if answer_state == 'Exit':
        break

    row = data[data["state"] == answer_state]

    if not row.empty:
        guessed_states.append(answer_state)
        x = row["x"].to_list()[0]
        y = row["y"].to_list()[0]
        writer.goto(x, y)
        writer.write(
            move=False,
            arg=f"{answer_state}",
            align=ALIGNMENT, font=FONT)


all_states = data["state"].to_list()
left_states = [state for state in all_states if state not in guessed_states]

dict = {
    "State": left_states
}

df = pandas.DataFrame(dict)
df.to_csv("states_to_learn.csv")
