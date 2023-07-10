from turtle import Turtle

FONT = ("Courier", 20, "normal")
FINAL_FONT = ("Courier", 40, "normal")


class LivesRemaining(Turtle):

    def __init__(self, position):
        super().__init__()
        self.color("black")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.pu()
        self.left(90)
        self.goto(position)


class Scoreboard(Turtle):

    def __init__(self, player):
        super().__init__()
        self.score = 0
        self.lives_remaining = []
        self.update_scoreboard(player)

    def update_scoreboard(self, player):
        self.clear()
        for lives in self.lives_remaining:
            lives.hideturtle()
        self.hideturtle()
        self.pu()
        self.goto(-270, 270)
        self.write(f"Score: {self.score}", font=FONT)
        self.goto(0, 270)
        self.write(f"Lives Remaining: ", font=FONT)
        new_xcor = 210
        self.setx(new_xcor)
        for _ in range(player.lives):
            position = (new_xcor, 290)
            lives = LivesRemaining(position)
            self.lives_remaining.append(lives)
            new_xcor += 30

    @staticmethod
    def clear_board(invader_lasers, player):
        # erase all invader lasers
        for inv_laser in invader_lasers:
            inv_laser.erase()
        invader_lasers.clear()  # clear invader_lasers list
        # remove player's lasers
        for player_laser in player.lasers:
            player_laser.erase()
        player.lasers.clear()  # clear the list of player lasers

    def player_win(self):
        self.goto(-120, 0)
        self.write("YOU WIN!!!", font=FINAL_FONT)

    def player_lose(self):
        self.goto(-120, 0)
        self.write("Game Over.", font=FINAL_FONT)
