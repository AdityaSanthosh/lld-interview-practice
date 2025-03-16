class Board:
    def __init__(self, snake_positions, ladder_positions):
        self.snake_locs = snake_positions
        self.ladder_locs = ladder_positions

        # board properties
        self.start_pos = 1
        self.end_pos = 100

    def update_pos(self, past_pos, places) -> int:
        new_pos = past_pos + places
        while (new_pos in self.ladder_locs) or (new_pos in self.snake_locs):
            if new_pos in self.ladder_locs:
                new_pos = self.ladder_locs[new_pos]
            if new_pos in self.snake_locs:
                new_pos = self.snake_locs[new_pos]
        return new_pos

    def is_end_of_board(self, pos):
        return pos == self.end_pos
