from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

# creating an instance of Screen class
screen = Screen()

# setting up the width and height of the screen
screen.setup(800, 600)

# changing the screen color to black
screen.bgcolor("black")

# set the title on the screen
screen.title("PONG GAME")
screen.tracer(0)

# creating instance of the imported class
t = Turtle()
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-360, 0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(r_paddle.move_Up, key="Up")
screen.onkey(r_paddle.move_Down, key="Down")
screen.onkey(l_paddle.move_Up, key="w")
screen.onkey(l_paddle.move_Down, key="s")

is_game_on = True
while is_game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move_ball()

    # detect collision with top and bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddles
    if (ball.xcor() > 320 and ball.distance(r_paddle) < 50) or (ball.xcor() < -320 and ball.distance(l_paddle) < 50):
        ball.speed_up()
        ball.bounce_x()

    # when ball misses the paddle and go out of boundary
    # for right-paddle
    if ball.xcor() > 380:
        ball.misses_paddle()
        scoreboard.l_score()

    # for left-paddle
    if ball.xcor() < -380:
        ball.misses_paddle()
        scoreboard.r_score()

screen.exitonclick()
