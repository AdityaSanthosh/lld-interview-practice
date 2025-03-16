from game import Game
from board import Board

if __name__ == "__main__":
    snakes = int(input())
    snakes_loc = {}
    for _ in range(snakes):
        head, tail = map(int, input().split())
        snakes_loc[head] = tail
    ladders = int(input())
    ladders_loc = {}
    for _ in range(ladders):
        start, end = map(int, input().split())
        ladders_loc[start] = end
    players = int(input())
    player_names = []
    for _ in range(players):
        player_names.append(input())
    new_game = Game(
        player_names, Board(snake_positions=snakes_loc, ladder_positions=ladders_loc)
    )
    new_game.simulate()
