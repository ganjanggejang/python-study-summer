# from turtle import *    --> 이렇게하면 turtle 안에 있는 모든 모듈을 불러옴, 좋은 방법은 아님
# import turtle as t      --> turtle을 여기선 t로 부름

from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")

for x in range(4):
    timmy.right(90)
    timmy.forward(100)

# 가장 마지막 부분에 있어야할 코드들
screen = Screen()
screen.exitonclick()