from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, direction):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        if direction == 'left':
            self.goto(-350, 0)
        else:
            self.goto(350, 0)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)
