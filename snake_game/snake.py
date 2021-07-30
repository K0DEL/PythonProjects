from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for _ in range(3):
            timmy = Turtle("square")
            timmy.color("white")
            timmy.penup()
            timmy.goto(-20 * _, 0)
            self.segments.append(timmy)

    def extend(self):
        timmy = Turtle("square")
        timmy.color("white")
        timmy.penup()
        x = self.segments[-1].xcor()
        y = self.segments[-1].ycor()
        timmy.goto(x, y)
        self.segments.append(timmy)

    def move(self):
        total_segments = len(self.segments) - 1
        for seg_num in range(total_segments, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(10)

    def up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(90)

    def down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(270)

    def left(self):
        if self.segments[0].heading() != RIGHT:
            self.segments[0].setheading(180)

    def right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(0)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
