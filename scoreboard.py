#Importing Libraries
from turtle import Turtle

# CONSTANTS
ALIGNMENT = 'center'
FONT = ('Arial', 12, 'normal')
COLOR = 'red'
X_INIT = 0
Y_INIT = 280
Y_INIT_GAME_OVER = 0
X_INIT_GAME_OVER = 0

class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        text = f"Score: {self.score}"
        self.penup()
        self.goto(X_INIT, Y_INIT)
        self.color(COLOR)
        self.hideturtle()
        self.write(text, align=ALIGNMENT, font=FONT)
        return
    
    def update_score(self):
        self.clear()
        self.score += 1
        text = f"Score: {self.score}"
        self.write(text, align=ALIGNMENT, font=FONT)
        return

    def game_over(self):
        self.goto(X_INIT_GAME_OVER,Y_INIT_GAME_OVER)
        self.write("GAME OVER", align= ALIGNMENT, font=FONT)
        return