from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

right_paddle = Paddle("right")
left_paddle = Paddle("left")

screen.listen()
screen.onkeypress(key="Up", fun=right_paddle.go_up)
screen.onkeypress(key="Down", fun=right_paddle.go_down)
screen.onkeypress(key="w", fun=left_paddle.go_up)
screen.onkeypress(key="s", fun=left_paddle.go_down)

ball = Ball()
score = Score()

is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    ball.move()
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320 or
            ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    if (ball.xcor() > 380):
        score.l_point()
        ball.reset_position()

    if (ball.xcor() < -380):
        score.r_point()
        ball.reset_position()

screen.exitonclick()
