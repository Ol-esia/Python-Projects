from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score_r_paddle = 0
        self.score_l_paddle = 0
        self.penup()
        self.hideturtle()
        self.color('white')

        self.update_scoreboard()


    def update_scoreboard(self):
        self.clear()
        self.score_r()
        self.score_l()

    def score_r(self):
        self.goto(50, 180)
        self.write(f"{self.score_r_paddle}", align='center', font=('Verdana', 50, 'bold'))

    def score_l(self):
        self.goto(-50, 180)
        self.write(f"{self.score_l_paddle}", align='center', font=('Verdana', 50, 'bold'))

    def refresh_score_r(self):
        self.score_r_paddle += 1
        self.update_scoreboard()

    def refresh_score_l(self):
        self.score_l_paddle += 1
        self.update_scoreboard()

