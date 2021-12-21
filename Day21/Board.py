class Board:

    def __init__(self, start_positions):
        self.valid_spaces = {1,2,3,4,5,6,7,8,9,10}
        self.max_space = 10
        self.start = start_positions.copy()
        self.player_positions = start_positions.copy()
        self.no_players = len(start_positions)

    def move(self, player_id, move):
        current_position = self.player_positions[player_id]
        new_position = current_position + move
        while new_position > self.max_space:
            new_position -= self.max_space
        self.player_positions[player_id] = new_position
        return new_position

