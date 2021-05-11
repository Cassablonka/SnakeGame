# Importing the required packages
from turtle import Turtle

# Setting up the constants
POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    # Initialising the Snake class
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Method to create the snake
    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    # Method to add segment to the snake after each food collision
    def add_segment(self, position):
        new_square = Turtle('square')
        new_square.color('white')
        new_square.penup()
        new_square.goto(position)
        self.segments.append(new_square)

    # Method to extend the snake's body
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Method to move the snake freely
    def move(self):
        for position in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[position - 1].xcor()
            new_ycor = self.segments[position - 1].ycor()
            self.segments[position].goto(new_xcor, new_ycor)
        self.head.forward(MOVE)

    # Method to move the snake up
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # Method to move the snake down
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # Method to move the snake left
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    # Method to move the snake right
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
