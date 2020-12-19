# ---IMPORTS---
from turtle import Screen
from config import *
from player import Player
from time import sleep
from cars import Car
from scoreboard import ScoreBoard


# ---FUNCTIONS---
def main():
    # Screen
    screen = Screen()
    screen.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
    screen.colormode(SCREEN_COLOR_MODE)
    screen.bgcolor(SCREEN_COLOR)
    screen.tracer(0)
    screen.listen()

    # Player
    player = Player()
    screen.onkey(player.moveUp, "Up")
    screen.onkey(player.moveRight, "Right")
    screen.onkey(player.moveLeft, "Left")

    # Cars
    cars = []

    # Score board
    scoreboard = ScoreBoard()
    scoreboard.writeScore(player_score=player.level)

    # Loop
    sleep_time = SCREEN_REFRESH_TIME
    game_is_on = True
    while game_is_on:

        screen.update()
        sleep(sleep_time)

        # Create the cars
        car = Car()
        for car_object in cars:
            car_object.moveCar()
        cars.append(car)
        if player.hasFinished():
            scoreboard.writeScore(player_score=player.level)
            sleep_time *= SLEEP_TIME_DECREASE_WHEN_FINISH
        # Erase car outside the screen
        for car in cars:
            if car.xcor() < -SCREEN_WIDTH / 2 - CAR_WIDTH / 2:
                cars.remove(car)
            # Detect crash
            crash = player.distance(car) < player.width()
            if crash:
                game_is_on = False
                scoreboard.gameOver()


    # Exit on click
    screen.exitonclick()


# --RUN---
if __name__ == "__main__":
    main()
