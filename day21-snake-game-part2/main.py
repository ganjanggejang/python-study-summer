from turtle import Screen
from snake import Snake  # 객체지향적으로 리팩토링하기
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Junsoo's Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()
    scoreboard.update_scoreboard()

    # 뱀이 먹이를 먹었을 때
    if snake.segments[0].distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_point()

    # 뱀이 벽에 부딪혔을 때
    if snake.segments[0].xcor() > 290 or snake.segments[0].xcor() < -290 or snake.segments[0].ycor() > 290 or snake.segments[0].ycor() < -290:
        scoreboard.reset()
        snake.reset()

    # 뱀의 머리가 몸통에 부딪혔을 때
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10:
            scoreboard.reset()

screen.exitonclick()
