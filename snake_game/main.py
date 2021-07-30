from turtle import Screen
import time
from snake import Snake
from food import Food
from score_board import Score

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

# with open("data.txt", "w") as file:
#     file.write("0")

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkeypress(key="Up", fun=snake.up)
screen.onkeypress(key="Down", fun=snake.down)
screen.onkeypress(key="Left", fun=snake.left)
screen.onkeypress(key="Right", fun=snake.right)


is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    if snake.segments[0].distance(food) < 15:
        score.update_score()
        food.refresh()
        snake.extend()

    if (snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or
            snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280):
        score.reset_score()
        snake.reset_snake()

    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 5:
            score.reset_score()
            snake.reset_snake()
screen.exitonclick()
