from turtle import Screen
from map_draw import Mapline
from paddle_move import Paddle
from map_ball import Ball
from score1 import Scoreboard1
from score2 import Scoreboard2
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


map_line = Mapline()
map_line.map_line_draw()
paddle = Paddle()
game_ball = Ball()
score_1 = Scoreboard1()
score_2 = Scoreboard2()

screen.listen()
screen.onkey(paddle.up_1, "Up")
screen.onkey(paddle.down_1, "Down")
screen.onkey(paddle.up_2, "w")
screen.onkey(paddle.down_2, "s")


game_is_on = True

while game_is_on:
    game_ball.ball_move()
    screen.update()
    time.sleep(0.1)
    if game_ball.ball1.ycor() > 280 or game_ball.ball1.ycor() < -280:
        if game_ball.ball1.heading() % 180 > 90:
            game_ball.ball_angle90()
            game_ball.ball_move()
            game_ball.ball_move()
        elif game_ball.ball1.heading() % 180 < 90:
            game_ball.ball_angle270()
            game_ball.ball_move()
            game_ball.ball_move()
    if game_ball.ball1.distance(paddle.paddle_1.xcor(), paddle.paddle_1.ycor() + 15) < 30 or game_ball.ball1.distance(paddle.paddle_2.xcor(), paddle.paddle_2.ycor() + 15) < 30 or game_ball.ball1.distance(paddle.paddle_1.xcor(), paddle.paddle_1.ycor() - 15) < 30 or game_ball.ball1.distance(paddle.paddle_2.xcor(), paddle.paddle_2.ycor() - 15) < 30:
        if game_ball.ball1.heading() % 180 > 90:
            game_ball.ball_angle270()
            game_ball.ball_move()
            game_ball.ball_move()
        elif game_ball.ball1.heading() % 180 < 90:
            game_ball.ball_angle90()
            game_ball.ball_move()
            game_ball.ball_move()
    if game_ball.ball1.xcor() > 290:
        score_1.increase_score()
        game_ball.ball_refresh()
        paddle.paddle_2.goto(280, 0)
        paddle.paddle_1.goto(-280, 0)

    elif game_ball.ball1.xcor() < -290:
        score_2.increase_score()
        game_ball.ball_refresh()
        paddle.paddle_2.goto(280, 0)
        paddle.paddle_1.goto(-280, 0)

    if score_1.score == 3:
        game_is_on = False
        score_1.game_over()
    elif score_2.score == 3:
        game_is_on = False
        score_2.game_over()


screen.exitonclick()

