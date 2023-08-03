from turtle import Turtle

class Scorecard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score=0
        self.penup()
        self.color("white")
        self.goto(0, 270)
        self.write(f"Score : {self.score}",align="center",font=("Arial",20,"normal"))

    def gameover(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 20, "normal"))


    def update(self):
        self.write(f"Score : {self.score}", align="center", font=("Arial", 20, "normal"))

    def increase(self):
        self.score+=1
        self.clear()
        self.update()