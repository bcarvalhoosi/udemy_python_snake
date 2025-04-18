from turtle import Turtle
import os
ALIGNEMENT = "center"
FONT=("Arial",24,'normal')

def write_score_to_file(high_score):
    with open("score_file.dat","w") as file:
        file.write(str(high_score))

def read_score_from_file():
    score = "0"
    if os.path.isfile("score_file.dat"):
        with open("score_file.dat") as file:
            score = file.read()
    else:
        with open("score_file.dat", "w") as file:
            file.write(score)
    return int(score)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-10,260)
        self.score = -1
         self.high_score = read_score_from_file()
        self.increase_score()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {str(self.score)} High Score: {str(self.high_score)}", move=False, align=ALIGNEMENT, font=FONT)

    # def game_over(self):
    #     self.goto(-10, 0)
    #     self.write(arg="GAME OVER!!!", move=False, align=ALIGNEMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            write_score_to_file(self.score)
        self.score = -1
        self.increase_score()