from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


screen.listen()
screen.onkey(key="space", fun=move_forwards) # 메소드에 ()괄호 붙이지 않는다
screen.exitonclick()