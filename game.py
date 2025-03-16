from random import randrange


def roll_dice():
    return randrange(2, 12)


class Game:
    def __init__(self, players, board):
        self.players = players
        self.curr_player = 0
        self.player_locs = {i: 0 for i in range(len(players))}
        self.board = board
        self.is_won = False

    def make_move(self, player, dice_value):
        player_pos = self.player_locs[player]

        if player_pos + dice_value > self.board.end_pos:
            print(
                f"{self.players[self.curr_player]} rolled a {dice_value} at {player_pos} preventing a move on the board"
            )
        else:
            new_pos = self.board.update_pos(player_pos, dice_value)
            self.player_locs[self.curr_player] = new_pos
            print(
                f"{self.players[self.curr_player]} rolled a {dice_value} and moved from #{player_pos} to {new_pos}"
            )
            if self.board.is_end_of_board(new_pos):
                print(f"{self.players[self.curr_player]} wins the game", self.board.snake_locs, self.board.ladder_locs)
                self.is_won = True
        self.curr_player = (self.curr_player + 1) % len(self.players)

    def simulate(self):
        curr_player = 0
        while not self.is_won:
            dice_value = roll_dice()
            self.make_move(curr_player, dice_value)
            curr_player = self.next_player(curr_player)

    def next_player(self, curr_player):
        return (curr_player + 1) % len(self.players)
