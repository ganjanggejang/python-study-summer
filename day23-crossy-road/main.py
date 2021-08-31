import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.title("Junsoo's Crossy road")
screen.setup(width=600, height=600)
screen.tracer(0)

screen.listen()
screen.onkey(player.press_up, "Up")
screen.onkey(player.press_left, "Left")
screen.onkey(player.press_right, "Right")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    scoreboard.update_scoreboard()
    car_manager.create_cars()
    car_manager.run_cars()

    if player.turtle.ycor() > 280:  # if 거북이가 결승선에 도착하면:
        car_manager.move_distance += 2  # 자동차 속도 증가
        car_manager.frequency += 10  # 자동차 개수 증가
        player.go_to_start_line()  # 거북이 원위치
        scoreboard.add_point()  # 점수 +1 추가

    for car in car_manager.all_cars:
        if player.turtle.distance(car) < 25:  # if 거북이가 자동차에 부딪히면
            game_is_on = False
            car_manager.all_cars.clear()
            scoreboard.game_over()

screen.exitonclick()
