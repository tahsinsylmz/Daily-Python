from turtle import Turtle


class Paddle():
    paddle_1 = Turtle()
    paddle_1.shape("square")
    paddle_1.shapetransform(0, -1, 4, 0)
    paddle_1.color("white")
    paddle_1.setheading(90)
    paddle_1.penup()
    paddle_2 = paddle_1.clone()
    paddle_2.goto(280, 0)
    paddle_1.goto(-280, 0)


    def up_1(self):
        self.paddle_1.setheading(90)
        self.paddle_1.forward(30)


    def down_1(self):
        self.paddle_1.setheading(270)
        self.paddle_1.forward(30)

    def up_2(self):
        self.paddle_2.setheading(90)
        self.paddle_2.forward(30)


    def down_2(self):
        self.paddle_2.setheading(270)
        self.paddle_2.forward(30)