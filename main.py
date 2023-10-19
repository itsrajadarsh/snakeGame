from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from border import Border
import time
import random

game_is_on = True
inc_scr = 1
screen = Screen()

# asking useer to select game mode
mode = screen.numinput("Press", "1 for Easy \n2 for Hard", 1, minval=1, maxval=2)

screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("SNAKE GAME by adraj")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
if mode == 2:
    border = Border()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

# looping through like refresh rate
while game_is_on:
    screen.update()

    # for making, it faster according to score
    s = len(snake.boxes)
    t = 0.05
    if s < 10:
        t = 0.2 - (s/100)
    elif s < 20:
        t = 0.1 - ((s-10)/200)

    time.sleep(t)
    snake.move()

    if mode == 2:
        # wall detection and game over for Hard Mode
        if snake.boxes[0].xcor() > 280 or snake.boxes[0].xcor() < -280 or snake.boxes[0].ycor() > 280 or snake.boxes[0].ycor() < -280:
            game_is_on = False
            score.game_over()
    else:
        # wall pass over for Easy mode
        y = snake.boxes[0].ycor()
        x = snake.boxes[0].xcor()
        if x > 280:
            snake.boxes[0].goto(x=-280, y=y)
        elif x < -280:
            snake.boxes[0].goto(x=280, y=y)
        elif y > 280:
            snake.boxes[0].goto(x=x, y=-280)
        elif y < -280:
            snake.boxes[0].goto(x=x, y=280)

    # food detection and score update
    if snake.boxes[0].distance(food) <= 15:
        for _ in range(inc_scr):
            score.increase_score()
        snake.extend(snake.boxes[-1].position())
        x = random.randint(1,100)
        if x % 3 == 0:
            food.big_refresh()
            inc_scr = 2
        else:
            food.refresh()
            inc_scr = 1


    # self collision detection and game over
    for box in snake.boxes[1:]:
        if snake.boxes[0].distance(box) < 15:
            game_is_on = False
            score.game_over()


screen.exitonclick()