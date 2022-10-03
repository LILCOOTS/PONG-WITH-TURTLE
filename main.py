import turtle
import random


win = turtle.Screen()
win.bgcolor('black')
win.title("PONG WITH TURTLE")
win.setup(width=1080, height=720)
win.tracer(0)

speed_list = [-0.5, 0.5]

# SCORE A AND B
player_a_score = 0
player_b_score = 0


# PADDLE A
paddle_a = turtle.Turtle()
paddle_a.shape("square")
paddle_a.speed(0)
paddle_a.color("red")
paddle_a.shapesize(stretch_len=1, stretch_wid=5)
paddle_a.penup()
paddle_a.goto(-490, 0)

# PADDLE B
paddle_b = turtle.Turtle()
paddle_b.shape("square")
paddle_b.speed(0)
paddle_b.color("blue")
paddle_b.shapesize(stretch_len=1, stretch_wid=5)
paddle_b.penup()
paddle_b.goto(490, 0)


# BALL
ball = turtle.Turtle()
ball.shape("circle")
ball.color("yellow")
ball.shapesize(stretch_len=1.5, stretch_wid=1.5)
ball.speed(3)
ball.penup()
ball.goto(0, 0)

ball.dx = random.choices(speed_list)[0]
ball.dy = random.choices(speed_list)[0]


# SCORE DISPLAY
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0, 300)
score.write("Player A: 0          Player B: 0",
            align="center", font=("Courier", 25, "normal"))


# WIN DISPLAY
won = turtle.Turtle()
won.speed(0)
won.color("white")
won.penup()
won.hideturtle()
won.goto(0, 200)


# MOVEMENT FUNCTION
def paddle_a_up():
    y = paddle_a.ycor()
    y += 25
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 25
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 25
    paddle_b.sety(y)


def paddle_b_down():
    y = paddle_b.ycor()
    y -= 25
    paddle_b.sety(y)

def game_start():
    return True
    

# KEYBOARD BINDING
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")


# Main Game
while True:
    win.update()

    # WIN DETERMINING STEP
    if player_a_score == 5:
        ball.goto(0, 0)
        paddle_a.goto(-490, 0)
        paddle_b.goto(490, 0)
        won.write("PLAYER A WINS!!!!", align="center",
                  font=("Courier", 30, "normal"))
    if player_b_score == 5:
        ball.goto(0, 0)
        paddle_a.goto(-490, 0)
        paddle_b.goto(490, 0)
        won.write("PLAYER B WINS!!!!", align="center",
                  font=("Courier", 30, "normal"))

    # BALL MOVEMENT
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # BORDER DETECTION
    if ball.ycor() > 340:
        ball.sety(340)
        ball.dy *= -1

    if ball.ycor() < -340:
        ball.sety(-340)
        ball.dy *= -1

    if ball.xcor() > 510:
        ball.goto(0, 0)
        ball.dx *= -1
        player_a_score += 1
        score.clear()
        score.write(f"Player A: {player_a_score}          Player B: {player_b_score}",
                    align="center", font=("Courier", 25, "normal"))

    if ball.xcor() < -510:
        ball.goto(0, 0)
        ball.dx *= -1
        player_b_score += 1
        score.clear()
        score.write(f"Player A: {player_a_score}          Player B: {player_b_score}",
                    align="center", font=("Courier", 25, "normal"))

    if paddle_a.ycor() > 310:
        paddle_a.sety(310)

    if paddle_a.ycor() < -310:
        paddle_a.sety(-310)

    if paddle_b.ycor() > 310:
        paddle_b.sety(310)

    if paddle_b.ycor() < -310:
        paddle_b.sety(-310)

    # COLLISION DETECTION
    if (ball.xcor() > 470 and ball.xcor() < 490) and (ball.ycor() < paddle_b.ycor() + 60 and ball.ycor() > paddle_b.ycor() - 60):
        ball.setx(470)
        ball.dx *= -1

    if (ball.xcor() < -470 and ball.xcor() > -490) and (ball.ycor() < paddle_a.ycor() + 60 and ball.ycor() > paddle_a.ycor() - 60):
        ball.setx(-470)
        ball.dx *= -1

# ---------------------------------------------------------------------------------------------------------------------------------------
