from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("white")
        self.setheading(90)
        self.penup()
        self.goto(0, -280)

    def up(self):
        if self.ycor() < 280:
            y = self.ycor() + 10
            self.goto(0, y)
    
    def down(self):
        if self.ycor() < 280 and self.ycor() > -280:
            y = self.ycor() - 10
            self.goto(0, y)

    def finish_line(self):
        if self.ycor() >= 280:
            return True
        else:
            return False