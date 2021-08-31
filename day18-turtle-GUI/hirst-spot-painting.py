from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("circle")
timmy.color("blue")


def pick_color():
    colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    random.shuffle(colors)
    return colors[0]


timmy.penup()
for y in range(-200, 200, 40):
    for x in range(-200, 200, 40):
        timmy.goto(x, y)
        timmy.dot(20)
        timmy.color(pick_color())


# 가장 마지막 부분에 있어야할 코드들
screen = Screen()
screen.exitonclick()
