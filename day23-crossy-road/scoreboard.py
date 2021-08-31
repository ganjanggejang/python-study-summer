from turtle import Turtle
FONT = ("Arial", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.goto(-20, 280)
        self.color("deep pink")
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Stage {self.score}")

    def add_point(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.goto(-150, 0)
        self.write(f"Game Over. Your Score: {self.score}", font=("Arial", 20))
