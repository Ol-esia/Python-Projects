from turtle import Screen
from snake import Snake
import time
from food import Food
from scoreboard import Score


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()


game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")


    if snake.head.distance(food) < 15:
        food.refresh()
        score.refresh()
        snake.extend()

    if snake.segments[1].xcor() > 280 or snake.segments[1].xcor() < -280 or snake.segments[1].ycor() > 280 or snake.segments[1].ycor() < -280:
        game_is_on = False
        score.game_over()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.game_over()
            game_is_on = False

screen.exitonclick()
