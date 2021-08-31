from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")


def pick_color():
    colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    random.shuffle(colors)
    return colors[0]


for x in range(3, 50):
    for i in range(0, x):
        timmy.forward(50)
        timmy.right(360 / x)
    timmy.color(pick_color())

# 가장 마지막 부분에 있어야할 코드들
screen = Screen()
screen.exitonclick()