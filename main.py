import time
from turtle import Screen
from board import Board
from player import Player
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

board = Board()
player = Player()
scoreboard = Scoreboard(player)
invader_lasers = board.invader_lasers

screen.onkey(player.go_left, 'Left')
screen.onkey(player.go_right, 'Right')
screen.onkey(player.shoot, 'space')

counter = 0
while True:
    counter += 1
    screen.tracer(0)
    if board.get_bottom_invaders() == True:
        scoreboard.clear_board(invader_lasers, player)
        screen.update()
        scoreboard.player_lose()
        break
    board.check_speed()
    board.maybe_shoot(player)
    if board.check_player_laser_collisions(player.lasers, scoreboard):
        scoreboard.update_scoreboard(player)
        if len(board.all_invaders) == 0:
            scoreboard.clear_board(invader_lasers, player)
            screen.update()
            scoreboard.player_win()
            break
    for laser in invader_lasers:
        laser.move()
    for laser in player.lasers:
        laser.move()  # move each laser bolt in the list
    if board.speed >= 1:
        if counter % board.speed == 0:
            board.move_invader()
    else:
        board.move_invader()
    if board.check_invader_laser_collisions(player):
        scoreboard.clear_board(invader_lasers, player)
        if player.lives == 0:
            player.lose_life()
            screen.update()
            scoreboard.player_lose()
            break
        player.lose_life()
        screen.update()
        time.sleep(2)
        player.player_reset()
        scoreboard.update_scoreboard(player)
    screen.update()
    screen.listen()


screen.exitonclick()
