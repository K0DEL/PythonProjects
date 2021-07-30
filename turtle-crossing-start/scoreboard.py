from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.score = 0
        self.write(move=False, arg=f"Level: {self.score}", font=FONT)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(move=False, arg=f"Level: {self.score}", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(move=False, arg="Game Over", font=FONT)
