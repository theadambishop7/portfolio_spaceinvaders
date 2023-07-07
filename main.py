from turtle import Screen
from invaders_manager import Invader, Board
from player import Player


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

board = Board()
player = Player()
lasers = []

screen.onkey(player.go_left, 'Left')
screen.onkey(player.go_right, 'Right')


def shoot():
    laser = player.shoot()  # create a new laser bolt
    lasers.append(laser)  # add the new laser bolt to the list


screen.onkey(shoot, 'space')

counter = 0
while True:
    counter += 1
    screen.tracer(0)
    for laser in lasers:
        laser.move()  # move each laser bolt in the list
    if counter > 0:
        if counter % board.speed == 0:
            board.move_invader()
    else:
        board.move_invader()
    screen.update()
    screen.listen()



screen.exitonclick()
