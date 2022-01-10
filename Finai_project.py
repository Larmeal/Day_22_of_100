# สร้างเกม Pong

from turtle import Turtle, Screen, position, right
from paddle import Paddle
from ball import Ball
from Scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

scoreboard = Scoreboard()
ball = Ball()

# กำหนดให้ paddle แต่ละฝ่ายอยู่ที่ตำแหน่งอะไร โดยให้ class _ _ init_ _ กำหนด (self, position) เพื่อที่จะใส่ตำแหน่งของทั้ง สองฝ่ายโดยที่ใช้แค่ class เดียว
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# สร้างการควบคุมทั้งสองฝ่าย
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

again = True
while again:
    # บังคับให้ลูกบอลไม่วิ่งเร็วจนเกินไป
    time.sleep(ball.move_speed)
    # ทำให้ภาพมัน delay น้อยลง
    screen.delay(0)
    # อัพเดทหน้าจอ screen อยู่ตลอดเวลา
    screen.update()
    ball.move()

    # ถ้ากรณีที่ลูกบอกไปชนขอบด้านบน หรือด้านล่าง ลูกบอลจะเด้งออก
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # ถ้ากรณีที่ลูกบอลเด้งไปชนกับ paddle จะทำให้ลูกบอลเด้งกลับ
    if ball.distance(r_paddle) < 50 and ball.xcor() > 340 or ball.distance(l_paddle) < 50 and ball.xcor() < -340:
        ball.bounce_x()

    # ถ้าหากลูกบอลเลยพื้นที่ด้านหลังไปก็จะทำให้อีกฝ่ายได้คะแนนไป
    if ball.xcor() > 380:
        ball.reset_ball()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_ball()
        scoreboard.r_point()


screen.exitonclick()
 