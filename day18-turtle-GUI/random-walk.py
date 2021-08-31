from turtle import Turtle, Screen
import random


def pick_color():
    colors = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    random.shuffle(colors)
    return colors[0]


def pick_angle():
    angle = [0, 90, 180, 270]
    random.shuffle(angle)
    return angle[0]


timmy = Turtle()
timmy.shape("square")
timmy.shapesize(0.1)
timmy.color("blue")
timmy.pensize(10)
timmy.speed("fastest")

while True:
    timmy.forward(20)
    timmy.right(pick_angle())
    timmy.color(pick_color())

# 가장 마지막 부분에 있어야할 코드들
screen = Screen()
screen.exitonclick()
