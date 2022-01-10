from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.04

    def move(self):
        # เป็นการทำให้ลูกบอลเริ่มเคลื่อนที่จากตำแหน่งที่กำหนด ซึ่งการกำหนด x_move, y_move นั้นส่่่งผมให้ เราสามารถปรับแต่งการเคลื่อนที่ของลูกบอลได้
        position_x = self.xcor() + self.x_move
        position_y = self.ycor() + self.y_move
        self.goto(position_x, position_y)

    def bounce_y(self):
        # เป็นแนวคิดที่ชอบมากนั้นก็คือการสะท้อนให้ลูกบอลนั้นเด้งกลับไปทางทิศตรงกันข้ามในแนวแกน Y
        self.y_move *= -1

    def bounce_x(self):
        # เป็นแนวคิดที่ชอบมากนั้นก็คือการสะท้อนให้ลูกบอลนั้นเด้งกลับไปทางทิศตรงกันข้ามในแนวแกน X
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_ball(self):
        # เป็นการเริ่มต้นใหม่หลังจากรู้ผลแพ้ - ชนะ
        self.goto(0, 0)
        self.move_speed = 0.04
        # เมื่อเริ่มเกมลูกบอลจะพุ่งไปในทางตรงกันข้ามกับตาก่อนหน้า
        self.bounce_x()