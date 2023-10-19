from turtle import Turtle

class Border(Turtle):
    def __init__(self):
        super().__init__()
        self.width(10)
        self.color("brown")
        self.draw()

    def draw(self):
        self.penup()
        self.goto(300,300)
        self.pendown()
        self.setheading(180)
        self.forward(600)
        self.setheading(270)
        self.forward(600)
        self.setheading(0)
        self.forward(600)
        self.setheading(90)
        self.forward(600)
        self.penup()

