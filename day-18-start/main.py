from turtle import Turtle, Screen
import turtle
import random

turtle.colormode(255)
timmy = Turtle()
timmy.shape("turtle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def move_right():
    timmy.right(10)


def move_left():
    timmy.left(10)


def clear_screen():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen = Screen()
screen.listen()
screen.onkeypress(key="w", fun=move_forward)
screen.onkeypress(key="s", fun=move_backward)
screen.onkeypress(key="a", fun=move_left)
screen.onkeypress(key="d", fun=move_right)
screen.onkeypress(key="c", fun=clear_screen)
screen.exitonclick()
