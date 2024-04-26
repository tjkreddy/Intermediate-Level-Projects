from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.color("white")
        self.write(f"score = {self.score}", align="center", font=("Arial", 20, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 28, "normal"))

    def increase_score(self):
        self.clear()
        self.score += 1
        self.write(f"score = {self.score}", align="center", font=("Arial", 20, "normal"))
