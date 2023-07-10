from turtle import Turtle


PLAYER_SPEED = 10
LASER_SPEED = 15
STARTING_POSITION = (0, -260)


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.pu()
        self.goto(STARTING_POSITION)
        self.left(90)
        self.lasers = []
        self.lives = 3
        self.last_hit_time = 0

    def go_left(self):
        new_xcor = self.xcor() - PLAYER_SPEED
        self.setx(new_xcor)

    def go_right(self):
        new_xcor = self.xcor() + PLAYER_SPEED
        self.setx(new_xcor)

    def shoot(self):
        pos = self.position()
        laser = LaserBolt(pos)
        self.lasers.append(laser)  # add the new laser bolt to the list

    def lose_life(self):
        self.lives -= 1
        self.color("red")

    def player_reset(self):
        self.color("black")
        self.goto(STARTING_POSITION)
        self.lasers = []


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

    def erase(self):
        self.hideturtle()
