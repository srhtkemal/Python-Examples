import turtle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Left Paddel
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")  # 20x20 pixels
left_paddle.shapesize(stretch_len=1, stretch_wid=5)
left_paddle.color("white")
left_paddle.penup()
left_paddle.goto(-350, 0)
left_paddle_score = 0

# Right Paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.shapesize(stretch_len=1, stretch_wid=5)
right_paddle.color("white")
right_paddle.penup()
right_paddle.goto(350, 0)
right_paddle_score=0


# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.shapesize(stretch_len=1, stretch_wid=1)
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = float(0.2)
ball.dy = float(0.2)

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Left Player:{left_paddle_score}    Right Player:{right_paddle_score} ",
          align="center", font=("Courier", 24, "normal"))


def left_paddle_up():
    y = left_paddle.ycor()
    y += 30
    # left_paddle.goto(-350, y)
    left_paddle.sety(y)


def left_paddle_down():
    y = left_paddle.ycor()
    y -= 30
    # left_paddle.goto(-350, y)
    left_paddle.sety(y)


def right_paddle_up():
    y = right_paddle.ycor()
    y += 30
    # right_paddle.goto(-350, y)
    right_paddle.sety(y)


def right_paddle_down():
    y = right_paddle.ycor()
    y -= 30
    # right_paddle.goto(-350, y)
    right_paddle.sety(y)


wn.listen()
wn.onkeypress(left_paddle_up, "w")
wn.onkeypress(left_paddle_down, "s")
wn.onkeypress(right_paddle_up, "Up")
wn.onkeypress(right_paddle_down, "Down")

# Main Game Loop
while True:
    wn.update()
    # Ball Move
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    if (ball.ycor() > 290):
        ball.dy *= int(-1)

    if (ball.ycor() < -290):
        ball.dy *= int(-1)

    if (ball.xcor() > 400):
        left_paddle_score += 1
        pen.clear()
        pen.write(f"Left Player:{left_paddle_score}    Right Player:{right_paddle_score} ",
          align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= int(-1)

    if (ball.xcor() < -390):
        right_paddle_score += 1
        pen.clear()
        pen.write(f"Left Player:{left_paddle_score}    Right Player:{right_paddle_score} ",
          align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= int(-1)

    if (ball.xcor() > 340 and
        ball.xcor() < 350 and
        ball.ycor() < right_paddle.ycor() + 40 and
            ball.ycor() > right_paddle.ycor() - 40):
        ball.dx *= -1
    if (ball.xcor() < -340 and
        ball.xcor() > -350 and
        ball.ycor() > left_paddle.ycor() - 40 and
            ball.ycor() < left_paddle.ycor() + 40):
        ball.dx *= -1
     # Paddle - Ball Collision
