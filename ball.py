#Imports
from turtle import Turtle

# Class
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    # Movement Method
    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    # Bouncing Method
    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1
        self.move_speed *= 0.9

    # Track Movement Methods
    def pos_x(self):
        x = self.xcor()
        return x
    
    def pos_y(self):
        y = self.ycor()
        return y 
    
    # Reset to Original Position
    def reset(self):
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()