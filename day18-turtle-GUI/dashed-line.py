from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("blue")

for _ in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()


# 가장 마지막 부분에 있어야할 코드들
screen = Screen()
screen.exitonclick()