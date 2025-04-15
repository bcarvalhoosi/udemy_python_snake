from turtle import Turtle
ALIGNEMENT = "center"
FONT=("Arial",24,'normal')

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-10,260)
        self.score = 0
        self.write(arg="Score: " + str(self.score),move=False,align=ALIGNEMENT,font=FONT)
    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg="Score: " + str(self.score), move=False, align=ALIGNEMENT, font=FONT)
    def game_over(self):
        self.goto(-10, 0)
        self.write(arg="GAME OVER!!!", move=False, align=ALIGNEMENT, font=FONT)