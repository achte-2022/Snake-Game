#Importing Libraries
from turtle import Turtle
import random

#Constants
SHAPE = 'circle'
COLOR = 'green'
SPEED = 'fastest'
LENGTH_FACTOR = 0.75
WIDTH_FACTOR = 0.75
MIN_X = -280
MIN_Y = -280
MAX_X = 280
MAX_Y = 280


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape(SHAPE)
        self.penup()
        self.shapesize(stretch_len=LENGTH_FACTOR, stretch_wid=WIDTH_FACTOR)
        self.color(COLOR)
        self.speed(SPEED)
        self.reset_pos()
        return

    def reset_pos(self):
        random_x = random.randint(MIN_X, MAX_X)
        random_y = random.randint(MIN_Y, MAX_Y)
        self.goto(random_x, random_y)
        return