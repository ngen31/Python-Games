# This is a simple pong game

# Course by @TokyoEdTech

import turtle
import elements
import os
import winsound



# Create window
wn = turtle.Screen()
wn.title("Pong by migo")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)
file = 'bounce.wav'

# Score
score_a = 0
score_b = 0

# Create paddles and ball
paddle_1 = elements.Paddle(0)
paddle_2 = elements.Paddle(1)
ball = elements.ball()
ball.dx = 0.15
ball.dy = 0.15

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_1.up, "w")
wn.onkeypress(paddle_1.down, "s")
wn.onkeypress(paddle_2.up, "Up")
wn.onkeypress(paddle_2.down, "Down")


# Main Game Loop
while True:
    wn.update()

    # Move the ball
    #ball.move()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Borer checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        #os.system("mpg123 " + file)
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        #os.system("mpg123 " + file)
    if ball.xcor() > 390:
        score_a += 1
        ball.goto(0,0)
        ball.dx *= -1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -390:
        score_b += 1
        ball.goto(0,0)
        ball.dx *= -1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        #os.system("mpg123 " + file)
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
        #os.system("mpg123 " + file)

