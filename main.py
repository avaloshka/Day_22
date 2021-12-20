from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.listen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))


ball = Ball()
scoreboard = Scoreboard()
TIME = 0.1


screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")
screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(TIME)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 285 or ball.ycor() < -285:
        # Needs to bounce
        ball.bounce_y()
    # Detect collision with paddle
    elif ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()
        TIME = 0.1
    # Detect r_paddle misses
    elif ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    # Detect l_paddle misses
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
