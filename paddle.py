from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, pos):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=6, stretch_len=1)
        self.fillcolor("white")
        self.create_paddle(pos)

    def create_paddle(self, pos):
        self.goto(pos)

    def move_Up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_Down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
