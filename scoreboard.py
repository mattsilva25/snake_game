from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 18, "normal")


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_up = 0
        with open("data.txt") as data:
            self.new_high_score = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score_up} High Score: {self.new_high_score}", False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score_up > self.new_high_score:
            self.new_high_score = self.score_up
            with open("data.txt", mode="w") as data:
                data.write(f"{self.new_high_score}")
        self.score_up = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score_up += 1
        self.update_scoreboard()



