# ---IMPORTS---
from turtle import Turtle
from random import choice, randint
from config import *


# ---PRE-FUNCTIONS---
def positioning():
    y_positions_list = []
    range_start = int(-SCREEN_HEIGHT / 2 + PLAYER_WIDTH * 2)
    range_end = int(SCREEN_HEIGHT / 2 - PLAYER_WIDTH / 2 + 1)
    for y_position in range(range_start, range_end, PLAYER_WIDTH):
        y_positions_list.append(y_position)
    return y_positions_list


#    return car_speed


# ---CLASSES---
class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape(CAR_SHAPE)
        self.speed(CAR_SPEED)
        self.turtlesize(stretch_wid=CAR_STRETCH_WIDTH,
                        stretch_len=CAR_STRETCH_LEN)
        self.colorize()
        self.y_available_positions = positioning()
        self.startingPoint()
        self.car_speed = CAR_MOVEMENT_SPEED
        self.moveCar()

    def colorize(self):
        red = randint(0, 255)
        green = randint(0, 255)
        blue = randint(0, 255)
        self.color(red, green, blue)

    def startingPoint(self):
        new_x = SCREEN_WIDTH / 2
        new_y = choice(self.y_available_positions)
        self.goto(new_x, new_y)

    def eraseCar(self):
        if self.xcor() < -SCREEN_WIDTH / 2 - CAR_WIDTH / 2:
            self.reset()

    def moveCar(self):
        new_x = self.xcor() - self.car_speed
        self.goto(new_x, self.ycor())
