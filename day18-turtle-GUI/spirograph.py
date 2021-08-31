from turtle import Turtle, Screen
import random


def pick_color():
    colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    random.shuffle(colors)
    return colors[0]


timmy = Turtle()
timmy.speed("fastest")


def draw(gap):
    for _ in range(int(360 / gap)):
        timmy.color(pick_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + 10)


draw(2)

# 가장 마지막 부분에 있어야할 코드들
screen = Screen()
screen.exitonclick()