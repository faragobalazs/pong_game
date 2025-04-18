#Imports
from turtle import Turtle

# Constants
SPEED = 10

# Class
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()

    # Movement
    def move(self):
        new_x = self.xcor() + SPEED
        new_y = self.ycor() + SPEED
        self.goto(new_x, new_y)