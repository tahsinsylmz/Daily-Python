from turtle import Turtle
import random

class Ball():
    ball1 = Turtle()
    ball1.shape("circle")
    ball1.color("white")
    ball1.left(random.randint(110, 160))
    ball1.penup()



    def ball_refresh(self):
        self.ball1.home()
        self.ball1.left(random.randint(110, 160))

    def ball_angle90(self):
        self.ball1.setheading(self.ball1.heading() + 90)

    def ball_angle270(self):
        self.ball1.setheading(self.ball1.heading() + 270)

    def ball_move(self):
        self.ball1.forward(20)


