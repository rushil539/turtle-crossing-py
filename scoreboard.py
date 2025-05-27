from turtle import Turtle

FONT = ("Courier", 14, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(-250, 280)
        self.level = 1
        self.write(f"LEVEL: {self.level}", False, "center", FONT)
    
    def level_up(self):
        self.clear()
        self.level += 1
        self.write(f"LEVEL: {self.level}", False, "center", FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, "center", FONT)
        