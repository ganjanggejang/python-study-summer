from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player:
    def __init__(self):
        self.turtle = Turtle("turtle")
        self.turtle.color("black")
        self.turtle.penup()
        self.turtle.goto(STARTING_POSITION)
        self.turtle.setheading(90)

    def press_up(self):
        self.turtle.setheading(90)
        self.turtle.forward(MOVE_DISTANCE)

    def press_left(self):
        self.turtle.setheading(180)
        self.turtle.forward(MOVE_DISTANCE)

    def press_right(self):
        self.turtle.setheading(0)
        self.turtle.forward(MOVE_DISTANCE)

    def go_to_start_line(self):
        self.turtle.goto(STARTING_POSITION)

