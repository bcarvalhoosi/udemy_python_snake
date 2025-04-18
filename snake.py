from email.quoprimime import body_check
from turtle import Turtle
MOVE_SEQUENCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
class Snake:
    def __init__(self):
        self.body = []
        self.pos = []
        self.tail = Turtle()
        for i in range(3):
            self.add1(init=0)
        self.head = self.body[0]
        self.tail = self.body[-1]

    def reset(self):
        self.body.clear()
        self.pos.clear()
        for i in range(3):
            self.add1(init=0)
        self.head = self.body[0]
        self.tail = self.body[-1]


    def add1(self,init):
        pos = len(self.body)
        self.body.append(Turtle(shape="square"))
        self.body[pos].color("white")
        self.body[pos].penup()
        if init==0:
            self.body[pos].goto(x=0 - 20 * pos, y=0)
        else:
            if self.tail.heading() in [DOWN,UP] :
                cor = (self.tail.xcor(),self.tail.ycor() -20)
            else:
                cor = (self.tail.xcor() -20, self.tail.xcor())
            self.body[pos].goto(cor)
        self.pos.append(self.body[pos].position())
        self.tail = self.body[-1]

    def move_forward(self):
        self.head.forward(MOVE_SEQUENCE)
        for i in range(1,len(self.body)):
            self.body[i].goto(self.pos[i-1])
        for i in range(0,len(self.body)):
            self.pos[i] = self.body[i].position()

    def increase_tail(self):
        self.add1(init=1)

    def hit_wall(self):
        if self.head.xcor() < -280 or self.head.xcor() > 280 or self.head.ycor() < -280 or self.head.ycor() > 280:
            return True

    def hit_tail(self):
        for item in self.body[1:]:
            return self.head.distance(item) < 15

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)