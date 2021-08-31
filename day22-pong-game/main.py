from turtle import Screen
from turtle import Turtle

screen = Screen()
paddle2 = Turtle()


screen.bgcolor("black")
screen.title("Ping Pong Game")
screen.setup(800, 600)

paddle2.shape("square")
paddle2.color("white")
paddle2.goto(350, 0)
paddle2.shapesize(stretch_wid=5, stretch_len=1)














screen.exitonclick()