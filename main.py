# Importing Libraries
from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Constants
X_MAX = 280
X_MIN = -280
Y_MIN = -280
Y_MAX = 279

# Screen Setup
window = Screen()
window.setup(width=600, height=600)
window.bgcolor("black")
window.title("Snake Game")
window.tracer(0)

# Objects Setup
snake = Snake()
food = Food()
scoreboard = ScoreBoard()


window.listen()
window.onkey(snake.up, "Up")
window.onkey(snake.down, "Down")
window.onkey(snake.left, "Left")
window.onkey(snake.right, "Right")
window.update()

# Turn on the game
game_is_on = True

while game_is_on:

    # Snake Movement
    window.update()
    time.sleep(0.1)
    snake.move()

    # Food Collision
    if snake.head.distance(food) < 15:
        food.reset_pos()
        snake.extend()
        scoreboard.update_score()

    # Wall Collision
    if (
        (snake.head.xcor() < X_MIN)
        or (snake.head.xcor() > X_MAX)
        or (snake.head.ycor() < Y_MIN)
        or (snake.head.ycor() > Y_MAX)
    ):
        scoreboard.game_over()
        time.sleep(1)
        scoreboard.game_reset()
        snake.game_reset()

    # Tail Collision
    for snake_block in snake.snake_list[1:]:
        if snake.head.distance(snake_block) < 10:
            scoreboard.game_over()
            time.sleep(1)
            scoreboard.game_reset()
            snake.game_reset()
window.exitonclick()
