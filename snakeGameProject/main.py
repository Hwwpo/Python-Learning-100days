from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
# 关闭动画效果，改为手动刷新屏幕显示
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # 吃食物
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # 检测出界
    if (snake.segments[0].xcor() > 290
            or snake.segments[0].xcor() < -290
            or snake.segments[0].ycor() > 290
            or snake.segments[0].ycor() < -290):
        game_is_on = False

    # 检测碰尾
    for segment in snake.segments[1:-1]:
        if snake.segments[0].distance(segment) < 10:
            game_is_on = False

scoreboard.game_over()

screen.exitonclick()
