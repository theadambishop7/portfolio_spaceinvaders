from invaders_manager import Invader, InvaderLaser
from turtle import Turtle
import time


MOVE_DISTANCE = 5
STARTING_DELAY = 50
SPEED_INCREASE = 2
LASER_SPEED = 10


class Shield(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=4, stretch_len=5)  # adjust as needed
        self.penup()
        self.health = 30
        self.goto(position)
        self.update_color()

    def update_color(self):
        if self.health > 15:
            self.color("slate gray")
        elif self.health > 5:
            self.color("peru")
        else:
            self.color("light coral")

    def erase(self):
        self.hideturtle()


class Board:
    def __init__(self):
        self.all_invaders = []
        self.all_shields = []
        self.invader_lasers = []
        self.total_starting_invaders = 0
        self.create_board()
        self.x_move = 1
        self.speed = STARTING_DELAY

    def check_speed(self):
        if len(self.all_invaders) < self.total_starting_invaders * 0.1:
            if self.speed > 10:
                self.speed = 10
        elif len(self.all_invaders) < self.total_starting_invaders * 0.50:
            if self.speed > 15:
                self.speed = 15
        elif len(self.all_invaders) < self.total_starting_invaders * 0.75:
            if self.speed > 30:
                self.speed = 30

    def create_board(self):
        rows = 6  # number of rows of invaders
        columns = 6  # number of invaders per row
        self.total_starting_invaders = rows * columns
        x_start = -230  # starting x position for the invaders
        y_start = 250  # starting y position for the invaders
        colors = ["lime", "lime", "gray", "gray", "black", "black"]
        health = [10, 10, 7, 7, 5, 5]
        point_value = [1000, 1000, 500, 500, 100, 100]
        for i in range(rows):
            x = x_start
            y = y_start
            for _ in range(columns):
                invader = Invader((x, y), health=health[i], point_value=point_value[i])
                invader.color(colors[i])  # cycle through the colors list
                self.all_invaders.append(invader)
                x += 80  # space between invaders
            y_start -= 25  # space between rows of invaders
        x2 = -210
        y2 = -190
        for _ in range(4):
            shield = Shield((x2, y2))
            self.all_shields.append(shield)
            x2 += 140

    def check_collision(self, ball):
        for invader in self.all_invaders:
            if ball.distance(invader) < 35:  # adjust this value based on your game's scale
                invader.erase()
                self.all_invaders.remove(invader)
                return True
        return False

    def move_invader(self):
        def find_xcor(unit):
            return unit.xcor()

        farthest_right = max(self.all_invaders, key=find_xcor)
        farthest_left = min(self.all_invaders, key=find_xcor)

        if farthest_right.xcor() > 280 or farthest_left.xcor() < -280:
            self.bounce()

        move_distance = MOVE_DISTANCE * self.x_move
        for invader in self.all_invaders:
            invader.forward(move_distance)

    def get_bottom_invaders(self):
        bottom_invaders = {}
        for invader in self.all_invaders:
            if invader.ycor() < -140:
                return True
            x = invader.xcor()
            if x not in bottom_invaders or invader.ycor() < bottom_invaders[x].ycor():
                bottom_invaders[x] = invader
        return bottom_invaders.values()

    def maybe_shoot(self, player):
        now = time.time()
        for invader in self.get_bottom_invaders():
            if now - invader.last_shot_time > invader.reload_time and now - player.last_hit_time > 2:
                laser = InvaderLaser(invader.position())
                self.invader_lasers.append(laser)
                invader.last_shot_time = now

    def check_player_laser_collisions(self, lasers, scoreboard):
        hit_any_invader = False  # new flag to check if any invader has been hit
        for laser in lasers:
            # Check collisions with invaders
            hit = False
            for invader in self.all_invaders:
                if laser.distance(invader) < 30:  # adjust this number as needed
                    invader.health -= 1
                    invader.update_color()
                    if invader.health <= 0:
                        invader.erase()
                        scoreboard.score += invader.point_value
                        self.all_invaders.remove(invader)
                    laser.erase()
                    lasers.remove(laser)
                    hit = True
                    hit_any_invader = True  # set the new flag to True if any invader is hit
                    break
            if hit:
                continue
            # Check collisions with shields
            for shield in self.all_shields:
                if laser.distance(shield) < 55:  # adjust this number as needed
                    shield.health -= 1
                    shield.update_color()
                    if shield.health <= 0:
                        shield.erase()
                        self.all_shields.remove(shield)
                    laser.erase()
                    lasers.remove(laser)
                    break
        return hit_any_invader

    def check_invader_laser_collisions(self, player):
        for laser in self.invader_lasers:
            if laser.distance(player) < 10:
                return True
            for shield in self.all_shields:
                if laser.distance(shield) < 55:  # adjust this number as needed
                    shield.health -= 1
                    shield.update_color()
                    if shield.health <= 0:
                        shield.erase()
                        self.all_shields.remove(shield)
                    laser.erase()
                    self.invader_lasers.remove(laser)
                    break

    def bounce(self):
        self.x_move *= -1
        self.drop()
        self.speed -= SPEED_INCREASE

    def drop(self):
        for invader in self.all_invaders:
            new_y = invader.ycor() - 10
            invader.sety(new_y)
