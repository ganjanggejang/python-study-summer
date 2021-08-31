from turtle import Turtle, Screen
import random
is_race_on = False
y_positions = [80, 50, 20, -10, -40, -70]
screen = Screen()
# keyword arguments(인자의 이름 써주고 값 넣기) vs positional arguments(정해진 순서대로 인자 값만 넣기)
screen.setup(width=540, height=440)  # keyword arguments
user_bet = screen.textinput(title="Make a bet!", prompt="당신의 거북이를 선택해주세요! Enter a color: \nred\norange\nyellow\ngreen\nblue\npurple")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

for n in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[n])
    new_turtle.penup()
    new_turtle.goto(x=-250, y=y_positions[n])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 237:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"맞췄다! {winning_color}색 거북이가 이겼습니다!")
            else:
                print(f"흑흑 못 맞췄어요. {winning_color}색 거북이가 이겼습니다..")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
