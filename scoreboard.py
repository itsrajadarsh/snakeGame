from turtle import Turtle
import time
from turtle import Screen
screen = Screen()


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.countdown = 3
        self.hideturtle()
        self.penup()
        self.color("white")
        self.countdown_time()
        self.goto(0, 270)
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!", align="center", font=("courier", 25, "normal"))

    def update_scoreboard(self):
        self.write(f"Score = {self.score}", align="center", font=("courier", 20, "normal"))

    def countdown_time(self):
        while self.countdown > 0:
            self.write(f"{self.countdown}", align="center", font=("courier", 30, "normal"))
            screen.update()
            time.sleep(1)
            self.countdown -= 1
            self.clear()
        self.goto(0, 270)

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_scoreboard()