# PONG GAME

from turtle import Turtle, Screen
from paddle import Paddle

# Screen Setup
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0) # turn off animation

paddle_right = Paddle()
paddle_left = Paddle()

paddle_right.goto(350, 0)
paddle_left.goto(-350,0)

screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")

# Screen Setup
game_is_on = True
while game_is_on:
  screen.update()

screen.exitonclick()