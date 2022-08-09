import time
import turtle
import pygame
from pygame import mixer


win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=800, height=600)
win.tracer(0)


# Score
score_a = 0
score_b = 0


# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()

ball.dx = 4
ball.dy = -2
ball.x = 0
ball.y = 0

# Mid Line
line = turtle.Turtle()
line.speed(0)
line.hideturtle()
line.color("white")
line.penup()
line.goto(0, -400)
line.pendown()
line.goto(0, 400)
line.penup()


# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center",
          font=("Courier", 24, "normal"))


# Functions


def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)


# Keybindings
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    win.update()
    time.sleep(1/60)

    # Border Checking
    if ball.ycor() > 290:
        ball.y = 290
        ball.dy *= -1

    if ball.ycor() < - 290:
        ball.y = -290
        ball.dy *= -1

    if ball.xcor() > 390:
        mixer.init()
        mixer.music.load("score.wav")
        mixer.music.set_volume(1)
        mixer.music.play()
        ball.x, ball.y = 0, 0
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b),
                  align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        mixer.init()
        mixer.music.load("score.wav")
        mixer.music.set_volume(1)
        mixer.music.play()
        ball.x, ball.y = 0, 0
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b),
                  align="center", font=("Courier", 24, "normal"))

    # Paddle/Ball collisions
    if ball.xcor() > 340 and ball.xcor() < 350 and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.x = 340
        ball.dx *= -1
        mixer.init()
        mixer.music.load("bounce.wav")
        mixer.music.set_volume(1)
        mixer.music.play()

    if ball.xcor() < -340 and ball.xcor() > -350 and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.x = -340
        ball.dx *= -1
        mixer.init()
        mixer.music.load("bounce.wav")
        mixer.music.set_volume(1)
        mixer.music.play()

    # Move ball
    ball.x += ball.dx
    ball.y += ball.dy
    ball.goto(ball.x, ball.y)
