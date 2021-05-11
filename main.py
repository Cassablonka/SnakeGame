# Importing the required modules
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

# Creating a screen to display our snake game
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# Creating score, snake, and food objects from the respective Classes
score = Score()
snake = Snake()
food = Food()

# Event listeners to tract the button clicks
screen.listen()
screen.onkey(fun=snake.up, key='Up')
screen.onkey(fun=snake.down, key='Down')
screen.onkey(fun=snake.left, key='Left')
screen.onkey(fun=snake.right, key='Right')

is_game_on = True

# Loop to keep the game on
while is_game_on:
    screen.update()
    time.sleep(.12)
    snake.move()

    # To detect the collision with the food
    if snake.head.distance(food) < 15:
        score.track_score()
        food.new_location()
        snake.extend()

    # To detect the collision with the screen's surface
    if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -290:
        is_game_on = False
        score.game_over()

    # To detect the collision with the snake's body
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            score.game_over()

screen.exitonclick()
