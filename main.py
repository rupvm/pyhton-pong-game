from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



screen=Screen()
screen.bgcolor("black")
screen.title("pong")
screen.setup(width=800,height=600)
screen.tracer(0)
screen.listen()

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
score=Scoreboard()


screen.onkeypress(fun=r_paddle.move_up, key="Up")
screen.onkeypress(fun=r_paddle.move_down, key="Down")
screen.onkeypress(fun=l_paddle.move_up, key="w")
screen.onkeypress(fun=l_paddle.move_down, key="s")


game_is_on=True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()


    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()

    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
        ball.bounce_x()

    #right paddle misses
    elif ball.xcor()>380:
        ball.ball_reset()
        score.l_point()

    #left paddle misses
    elif ball.xcor()<-380:
        ball.ball_reset()
        score.r_point()














screen.exitonclick()