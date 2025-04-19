# PONG GAME

# Imports
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

# Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0) # turn off animation

# Objects
r_paddle = Paddle()
l_paddle = Paddle()
ball = Ball()

# Original Positions
r_paddle.goto(350, 0)
l_paddle.goto(-350,0)
ball.goto(0,0)

# Paddle Control
screen.listen()
screen.onkeypress(r_paddle.move_up, "o")
screen.onkeypress(r_paddle.move_down, "l")
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")

# Screen Setup
game_is_on = True
while game_is_on:
  time.sleep(0.1)
  screen.update()
  ball.move()

  # Detect Collision with Wall

  if ball.ycor() > 280 or ball.ycor() < -280:
    ball.bounce_y()

  # Detect Collision with Right Paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()

  # Ball Pass Beyond Paddles
  if ball.xcor() == 400:
    ball.reset()

  if ball.xcor() == -400:
    ball.reset()

# Screen Setup
screen.exitonclick() 