#Importing Libraries
from turtle import Turtle

#Constants
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
X_INIT = 0
Y_INIT = 0
INIT_SNAKE_BLOCKS = 2


class Snake():
    def __init__(self):
        x_init = 0
        y_init = 0
        snake_block = Turtle(shape='square')
        snake_block.color('white')
        snake_block.penup()
        snake_block.goto(X_INIT, X_INIT)
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
        new_pos = self.snake_list[-1].pos()
        snake_block = Turtle(shape='square')
        snake_block.color('white')
        snake_block.penup()
        snake_block.goto(new_pos)
        self.snake_list.append(snake_block)
        return

    def up(self):
        current_heading = self.head.heading()
        if ((current_heading == UP) or (current_heading == DOWN)):
            return 
        else:
            self.head.setheading(UP)
            return

    def down(self):
        current_heading = self.head.heading()
        if ((current_heading == UP) or (current_heading == DOWN)):
            return 
        else:
            self.head.setheading(DOWN)
            return

    def left(self):
        current_heading = self.head.heading()
        if ((current_heading == RIGHT) or (current_heading == LEFT)):
            return 
        else:
            self.head.setheading(LEFT)
            return

    def right(self):
        current_heading = self.head.heading()
        if ((current_heading == RIGHT) or (current_heading == LEFT)):
            return 
        else:
            self.head.setheading(RIGHT)
            return