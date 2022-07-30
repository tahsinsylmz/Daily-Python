from turtle import Turtle


class Mapline():
    map_pen = Turtle()
    map_pen.pencolor("white")
    map_pen.hideturtle()
    def map_line_draw(self):
        super().__init__()
        self.map_pen.penup()
        self.map_pen.goto(0, -270)
        self.map_pen.pensize(5)
        self.map_pen.left(90)

        for line in range(19):
            self.map_pen.pendown()
            self.map_pen.fd(15)
            self.map_pen.penup()
            self.map_pen.fd(15)