
import another_module
print(another_module.another_variable)

import turtle
timmy = turtle.Turtle() #turtle 모듈(turtle.py)에 있는 Turtle 클래스로 timmy라는 객체를 만듦.

from turtle import Turtle, Screen #turtle 모듈에서 Turtle과 Screen만 가져옴. 가져오는 것은 클래스도 되고 함수(메서드)도 되고 그냥 변수(attribute)도 됨.
jessi = Turtle() #8번째줄처럼 불러오면 이렇게 모듈 이름 안붙이고 바로 사용 가능
print(jessi)
jessi.shape("turtle")
jessi.color("coral")


my_screen = Screen()
print(my_screen.canvheight, my_screen.canvwidth)
my_screen.exitonclick()
