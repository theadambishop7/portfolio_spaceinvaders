from turtle import Turtle


PLAYER_SPEED = 10
LASER_SPEED = 15

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.pu()
        self.goto(0, -240)
        self.left(90)

    def go_left(self):
        new_xcor = self.xcor() - PLAYER_SPEED
        self.setx(new_xcor)

    def go_right(self):
        new_xcor = self.xcor() + PLAYER_SPEED
        self.setx(new_xcor)

    def shoot(self):
        pos = self.position()
        laser = LaserBolt(pos)
        return laser  # return the created laser bolt


class LaserBolt(Turtle):

    def __init__(self, position):
        super().__init__()
        self.pu()
        self.goto(position)
        self.left(90)
        self.shape("square")
        self.color("red")
        self.shapesize(stretch_wid=.15, stretch_len=1.5)

    def move(self):
        self.forward(LASER_SPEED)
