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
paddle_right = Paddle()
paddle_left = Paddle()
ball = Ball()

# Original Positions
paddle_right.goto(350, 0)
paddle_left.goto(-350,0)
ball.goto(0,0)

# Paddle Control
screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")

# Screen Setup
game_is_on = True
while game_is_on:
  time.sleep(0.05)
  screen.update()
  ball.move()

screen.exitonclick()