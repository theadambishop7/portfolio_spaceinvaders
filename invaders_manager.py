from turtle import Turtle


MOVE_DISTANCE = 5
STARTING_DELAY = 50
SPEED_INCREASE = 5


class Invader(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.75, stretch_len=3)  # adjust as needed
        self.penup()
        self.goto(position)

    def erase(self):
        self.hideturtle()


class Board:
    def __init__(self):
        self.all_tiles = []
        self.create_board()
        self.x_move = 1
        self.speed = STARTING_DELAY

    def create_board(self):
        x_start = -230  # starting x position for the tiles
        y_start = 250  # starting y position for the tiles
        colors = ["lime", "lime", "gray", "gray", "black", "black"]
        for i in range(6):  # number of rows
            x = x_start
            y = y_start
            for _ in range(6):  # number of tiles per row
                tile = Invader((x, y))
                tile.color(colors[i])  # cycle through the colors list
                self.all_tiles.append(tile)
                x += 80  # space between tiles
            y_start -= 25  # space between rows

    def check_collision(self, ball):
        for tile in self.all_tiles:
            if ball.distance(tile) < 35:  # adjust this value based on your game's scale
                tile.erase()
                self.all_tiles.remove(tile)
                return True
        return False

    def move_invader(self):
        farthest_right = max(self.all_tiles, key=lambda invader: invader.xcor())
        farthest_left = min(self.all_tiles, key=lambda invader: invader.xcor())

        if farthest_right.xcor() > 280 or farthest_left.xcor() < -280:
            self.bounce()

        move_distance = MOVE_DISTANCE * self.x_move
        for invader in self.all_tiles:
            invader.forward(move_distance)

    def bounce(self):
        self.x_move *= -1
        self.drop()
        self.speed -= SPEED_INCREASE

    def drop(self):
        for invader in self.all_tiles:
            new_y = invader.ycor() - 10
            invader.sety(new_y)
