import time
from scoreboard import ScoreBoard

from snake import Snake
from turtle import Screen
from food import Food

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
my_snake = Snake()
food = Food()
scoreboard = ScoreBoard()
screen.update()
screen.listen()
screen.onkey(my_snake.up,"Up")
screen.onkey(my_snake.down,"Down")
screen.onkey(my_snake.left,"Left")
screen.onkey(my_snake.right,"Right")

game_is_on = True
while game_is_on:
    my_snake.move_forward()
    time.sleep(0.3)
    screen.update()
    if my_snake.hit_wall() or my_snake.hit_tail():
        #game_is_on = False
        scoreboard.reset()
        for body in my_snake.body:
            body.goto(1000,1000)
        my_snake.reset()

    if my_snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        my_snake.increase_tail()


screen.exitonclick()
