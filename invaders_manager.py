from turtle import Turtle
import random
import time

LASER_SPEED = 10


class Invader(Turtle):

    def __init__(self, position, health, point_value):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.75, stretch_len=3)  # adjust as needed
        self.penup()
        self.health = health
        self.initial_health = health
        self.point_value = point_value
        self.goto(position)
        self.last_shot_time = time.time()  # added this line
        self.reload_time = random.uniform(1, 5)  # added this line, adjust as necessary

    def update_color(self):
        if self.health <= self.initial_health * 0.3:
            self.color("red")
        elif self.health <= self.initial_health * 0.5:
            self.color("orange")

    def erase(self):
        self.hideturtle()


class InvaderLaser(Turtle):

    def __init__(self, position):
        super().__init__()
        self.pu()
        self.goto(position)
        self.right(90)
        self.shape("square")
        self.color("lime")
        self.shapesize(stretch_wid=.15, stretch_len=1.5)

    def move(self):
        self.forward(LASER_SPEED)

    def erase(self):
        self.hideturtle()
