# Importing Libraries
from turtle import Turtle

# CONSTANTS
ALIGNMENT = "center"
FONT = ("Arial", 12, "normal")
COLOR = "green"
X_INIT = 0
Y_INIT = 280
Y_INIT_GAME_OVER = 0
X_INIT_GAME_OVER = 0
HIGH_SCORE_FILE = "data.txt"


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.write_scoreboard()
        return

    def update_score(self):
        self.score += 1
        self.write_scoreboard()
        return

    def write_scoreboard(self):
        self.clear()
        self.penup()
        self.goto(X_INIT, Y_INIT)
        self.color(COLOR)
        self.hideturtle()
        text = f"Score: {self.score}    High Score: {self.high_score}"
        self.write(text, align=ALIGNMENT, font=FONT)
        return

    def game_reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.write_high_score()
        self.write_scoreboard()
        return

    def read_high_score(self):
        with open(HIGH_SCORE_FILE, "r") as file:
            high_score = int(file.read())
        return high_score

    def write_high_score(self):
        with open(HIGH_SCORE_FILE, "w") as file:
            file.write(str(self.high_score))
        return

    def game_over(self):
        self.goto(X_INIT_GAME_OVER, Y_INIT_GAME_OVER)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        return
