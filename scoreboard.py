# Importing the required packages
from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier', 20, 'normal')

class Score(Turtle):

    # Initialising the Score class
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt') as file:
            self.high_score = int(file.read())
        self.color('white')
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_score()

    # Method to update the score after each food collision
    def update_score(self):
        self.high_scored()
        self.write(f'Score: {self.score} High Score: {self.high_score}', False, align=ALIGNMENT, font=FONT)

    # Method to keep track of the highest score
    def high_scored(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode='w') as file:
                file.write(f'{self.high_score}')

    # Method to display Game Over after wall collision or head collision
    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align=ALIGNMENT, font=FONT)

    # Method to keep track of the score
    def track_score(self):
        self.score += 1
        self.clear()
        self.update_score()
