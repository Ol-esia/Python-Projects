from turtle import Turtle, Screen
import time
from scoreboard import Scoreboard
from paddle import Paddle
from ball import Ball

# Screen parameters
screen = Screen()
scoreboard = Scoreboard()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title("Pong Game")
screen_separator = Turtle()
screen_separator.color('white')
screen_separator.ht()
screen_separator.penup()
screen_separator.speed(0)

for _ in range(-270, 270, 40):
    screen_separator.goto(0, _)
    screen_separator.write(" l ", move=False, align="center", font=("Arial", 20, "normal"))

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

game_on = True

while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    screen.listen()
    ball.move()

    screen.onkey(r_paddle.go_up, "Up")
    screen.onkey(r_paddle.go_down, "Down")
    screen.onkey(l_paddle.go_up, "w")
    screen.onkey(l_paddle.go_down, "s")

    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 40 and ball.xcor() > 320:
        ball.bounce_x()
        scoreboard.refresh_score_r()

    if ball.distance(l_paddle) < 40 and ball.xcor() < - 320:
        ball.bounce_x()
        scoreboard.refresh_score_l()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.refresh_score_l()

    if ball.xcor() < - 380:
        ball.reset_position()
        scoreboard.refresh_score_r()

screen.exitonclick()
