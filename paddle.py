#Imports
from turtle import Turtle

# Constants
PADDLE_WIDTH_STRETCH = 5
PADDLE_LENGTH_SCRETCH = 1
MOVE_DISTANCE = 20

# Class
class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=PADDLE_WIDTH_STRETCH, stretch_len=PADDLE_LENGTH_SCRETCH)
        self.penup()

    # Moving Paddle Method
    def move_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y) 
