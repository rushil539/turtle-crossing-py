import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Turtle Crossing Game")
screen.listen()
screen.tracer(0)

player = Player()
car_list = []
score = Scoreboard()

screen.onkey(player.up, "Up")
screen.onkey(player.down, "Down")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    random_chance = random.randint(1,6)
    if random_chance == 1:
        car = CarManager()
        car_list.append(car)
    for cars in car_list:
        cars.move()
        if player.distance(cars) < 20:
            score.game_over()
            game_is_on = False
    if player.finish_line():
        score.level_up()
        car.dist_increment()
        player.goto(0, -280)

screen.exitonclick()