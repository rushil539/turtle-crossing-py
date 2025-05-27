from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 2)
        self.penup()
        self.color(random.choice(COLORS))
        self.y = random.randrange(-240, 241, 20)
        self.goto(300, self.y)
    
    def move(self):
        x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(x, self.y)

    def dist_increment(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += 10


    