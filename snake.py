from turtle import Turtle
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.boxes = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITION:
            self.extend(position)

    def extend(self, position):
        new_box = Turtle(shape="square")
        new_box.color("white")
        new_box.penup()
        new_box.goto(position)
        self.boxes.append(new_box)
        self.boxes[0].shape("triangle")

    def move(self):
        for i in range(len(self.boxes) - 1, 0, -1):
            x = self.boxes[i - 1].xcor()
            y = self.boxes[i - 1].ycor()
            self.boxes[i].goto(x=x, y=y)
        self.boxes[0].forward(MOVE_DISTANCE)
        # self.boxes[0].color("black")
        # self.boxes[0].shape("circle")



    def up(self):
        # print(self.boxes[0].getheading())
        if int(self.boxes[0].heading()) != 270:
            self.boxes[0].setheading(90)

    def down(self):
        if int(self.boxes[0].heading()) != 90:
            self.boxes[0].setheading(270)

    def left(self):
        if int(self.boxes[0].heading()) != 0:
            self.boxes[0].setheading(180)

    def right(self):
        if int(self.boxes[0].heading()) != 180:
            self.boxes[0].setheading(0)


