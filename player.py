# ---IMPORTS---
from turtle import Turtle
from config import *


# ---CLASSES---
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color(PLAYER_COLOR)
        self.shape(PLAYER_SHAPE)
        self.speed(PLAYER_SPEED)
        self.setheading(PLAYER_HEADING)
        self.startingPoint()
        self.score = 0
        self.level = 0

    def startingPoint(self):
        """
        Makes the player go to the initial starting point.
        """
        x_pos = PLAYER_INIT_X_POS
        y_pos = -SCREEN_HEIGHT / 2 + PLAYER_Y_DIST_TO_WALL
        self.goto(x_pos, y_pos)

    def moveUp(self):
        new_y = self.ycor() + PLAYER_MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def moveRight(self):
        limit_x = SCREEN_WIDTH / 2 - PLAYER_MOVE_DISTANCE
        if self.xcor() < limit_x:
            new_x = self.xcor() + PLAYER_MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def moveLeft(self):
        limit_x = -SCREEN_WIDTH / 2 + PLAYER_MOVE_DISTANCE
        if self.xcor() > limit_x:
            new_x = self.xcor() - PLAYER_MOVE_DISTANCE
            self.goto(new_x, self.ycor())

    def hasFinished(self):
        limit_top = SCREEN_HEIGHT / 2 - PLAYER_Y_DIST_TO_WALL
        if self.ycor() > limit_top:
            self.level += 1
            self.startingPoint()
            return True
        else:
            return False
