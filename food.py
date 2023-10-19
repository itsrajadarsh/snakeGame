from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color("yellow")
        self.shape("circle")
        x = random.randint(-280, 280)
        x -= (x % 20)
        y = random.randint(-280, 280)
        y -= (y % 20)
        self.goto(x, y)

    def big_refresh(self):
        self.color("red")
        self.shape("turtle")
        x = random.randint(-280, 280)
        x -= (x % 20)
        y = random.randint(-280, 280)
        y -= (y % 20)
        self.goto(x, y)