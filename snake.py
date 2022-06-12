# Importing Libraries
from turtle import Turtle
import random
import turtle

# Constants
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
DIRECTION = [UP, DOWN, LEFT, RIGHT]
X_INIT = 0
Y_INIT = 0
INIT_SNAKE_BLOCKS = 2
X_LIMIT = 600
Y_LIMIT = 600
HEAD_COLOR = "white"
SHAPE = "square"
MAX_INTENSITY = 255


class Snake:
    def __init__(self):
        self.create_snake()
        return

    def create_snake(self):
        snake_block = Turtle(shape=SHAPE)
        snake_block.color(HEAD_COLOR)
        snake_block.penup()
        snake_block.goto(X_INIT, X_INIT)
        random_direction = random.choice(DIRECTION)
        snake_block.setheading(random_direction)
        self.snake_list = [snake_block]
        self.head = snake_block
        for i in range(INIT_SNAKE_BLOCKS):
            self.extend()
        return

    def move(self):
        for block_index in range(len(self.snake_list) - 1, 0, -1):
            prev_x = self.snake_list[block_index - 1].xcor()
            prev_y = self.snake_list[block_index - 1].ycor()
            self.snake_list[block_index].goto(prev_x, prev_y)
        self.head.forward(MOVE_DISTANCE)
        return

    def extend(self):
        turtle.colormode(MAX_INTENSITY)
        new_pos = self.snake_list[-1].pos()
        snake_block = Turtle(shape=SHAPE)
        block_color = self.random_color()
        snake_block.color(block_color)
        snake_block.penup()
        snake_block.goto(new_pos)
        self.snake_list.append(snake_block)
        return

    def up(self):
        current_heading = self.head.heading()
        if (current_heading == UP) or (current_heading == DOWN):
            return
        else:
            self.head.setheading(UP)
            return

    def down(self):
        current_heading = self.head.heading()
        if (current_heading == UP) or (current_heading == DOWN):
            return
        else:
            self.head.setheading(DOWN)
            return

    def left(self):
        current_heading = self.head.heading()
        if (current_heading == RIGHT) or (current_heading == LEFT):
            return
        else:
            self.head.setheading(LEFT)
            return

    def right(self):
        current_heading = self.head.heading()
        if (current_heading == RIGHT) or (current_heading == LEFT):
            return
        else:
            self.head.setheading(RIGHT)
            return

    def game_reset(self):
        for snake_block in self.snake_list:
            snake_block.goto(x=X_LIMIT * 2, y=Y_LIMIT * 2)
        self.snake_list.clear()
        self.create_snake()
        return

    def random_color(self):
        red = random.randint(0, MAX_INTENSITY)
        green = random.randint(0, MAX_INTENSITY)
        blue = random.randint(0, MAX_INTENSITY)
        return (red, green, blue)
