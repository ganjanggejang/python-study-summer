from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.move_distance = 5  # 이동 거리 == 5
        self.frequency = 20  # 출현 빈도 == 20%

    def create_cars(self):
        random_chance = random.randint(0, 100)  # 자동차의 출현 빈도를 줄이기 위한 코드

        if random_chance in range(0, self.frequency):
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            new_car.setheading(180)
            self.all_cars.append(new_car)

    def run_cars(self):
        for car in self.all_cars:
            car.forward(self.move_distance)
