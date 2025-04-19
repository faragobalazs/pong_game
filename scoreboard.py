# Imports
from turtle import Turtle

# Class
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()
    
    # Update Scoreboard Method
    def update(self):
        self.clear()
        self.goto(-80, 200)
        self.write(self.l_score, align="center", font=("Courier", 70, "normal"))
        self.goto(80, 200)
        self.write(self.r_score, align="center", font=("Courier", 70, "normal"))

    # Addig Scores Methods
    def l_point(self):
        self.l_score += 1
        self.update()
    
    def r_point(self):
        self.r_score += 1
        self.update()


