from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = -1
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        with open("./python/snake_game/data.txt", "r") as file:
            self.high_score = int(file.read())
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(move=False, arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(
            move=False,
            arg=f"Score: {self.score} High Score: {self.high_score}",
            align=ALIGNMENT, font=FONT)

    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("./python/snake_game/data.txt", "w") as file:
                file.write(str(self.high_score))
        self.score = -1
        self.update_score()
