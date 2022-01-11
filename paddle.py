from turtle import Turtle

class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        # ขนาดที่กำหนดนี้จะคูณกับ อัตราส่วนของ Turtle นั้นก็คือ คูณ 20 pixel
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)
        

    def up(self):
        position_y = self.ycor() + 40
        self.goto(self.xcor(), position_y)

    def down(self):
        position_y = self.ycor() - 40
        self.goto(self.xcor(), position_y)

