import turtle
from turtle import Turtle

class Paddle:
    def __init__(self, position):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.shapesize(stretch_wid=5,stretch_len=1)
        self.paddle.color("white")
        self.paddle.penup()
        if position == 0:
            self.paddle.goto(-350, 0)
        else:
            self.paddle.goto(350, 0)

    def xcor(self):
        return self.paddle.xcor()

    def ycor(self):
        return self.paddle.ycor()

    def up(self):
        if self.paddle.ycor() > 240:
            self.paddle.sety(250)
        else:
            y = self.paddle.ycor() + 20
            self.paddle.sety(y)

    def down(self):
        if self.paddle.ycor() < -240:
            self.paddle.sety(-250)
        else:
            y = self.paddle.ycor() - 20
            self.paddle.sety(y)


class ball:
    def __init__(self):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("square")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(0, 0)

    def dx(self, dx):
        ball.dx = dx

    def dy(self, dy):
        ball.dy = dy

    def goto(self, x,y):
        self.ball.goto(x,y)
    def move(self):
        self.ball.setx(self.ball.xcor() + ball.dx)
        self.ball.sety(self.ball.ycor() + ball.dy)

    def setx(self, x):
        self.ball.setx(x)

    def sety(self, y):
        self.ball.sety(y)

    def xcor(self):
        return self.ball.xcor()

    def ycor(self):
        return self.ball.ycor()
'''
    def xcor(self):
        print("ball.xcor(): " + self.xcor())
        return self.xcor()
    def ycor(self):
        print("ball.ycor(): " + self.ycor())
        return self.ycor()
    def setx(self,x):
        self.setx(x)
    def sety(self,y):
        self.setx(y)
'''
