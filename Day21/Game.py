from Dice import Die
from Board import Board

class Game:

    def __init__(self,start_positions:list) -> None:
        self.no_players = len(start_positions)
        self.scores = []
        for _ in range(0, self.no_players):
            self.scores.append(0)
        self.winner = None
        self.winning_score = None
        self.die = Die()
        self.board = Board(start_positions)
    
    def play_game(self, target=1000) -> tuple:
        self.target_score = target
        while self.winner is None:
            self.play_round()
        if self.winner == 0:
            losing_score = self.scores[1]
        else:
            losing_score = self.scores[0]
        return losing_score, self.die.rolls

    def play_round(self) -> None:
        for player_id in range(0, self.no_players):
            if self.winner == None:
                self.take_turn(player_id)

    def take_turn(self, player_id) -> None:
        current_score = self.scores[player_id]
        turn_spaces = self.die.multi_roll(3)
        turn_score = self.board.move(player_id, turn_spaces)
        current_score += turn_score
        if current_score >= self.target_score:
            self.winning_score = current_score
            self.winner = player_id
        self.scores[player_id] = current_score
        



