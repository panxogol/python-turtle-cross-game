# ---IMPORTS---
from turtle import Turtle
from config import *


# ---CLASSES---
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color(SCOREBOARD_COLOR)

    def writeScore(self, player_score: int):
        self.clear()
        y_pos = SCREEN_HEIGHT / 2 - SCOREBOARD_TEXT_SIZE - PLAYER_WIDTH
        self.goto(self.xcor(), y_pos)
        text = f"Score: {player_score}"
        self.write(
            arg=text,
            align=SCOREBOARD_TEXT_ALIGN,
            font=(
                SCOREBOARD_TEXT_FONT,
                SCOREBOARD_TEXT_SIZE,
                SCOREBOARD_TEXT_STYLE
            )
        )

    def gameOver(self):
        self.home()
        self.write(
            arg=GAME_OVER_TEXT,
            align=GAME_OVER_TEXT_ALIGN,
            font=(
                GAME_OVER_TEXT_FONT,
                GAME_OVER_TEXT_SIZE,
                GAME_OVER_TEXT_STYLE
            )
        )
