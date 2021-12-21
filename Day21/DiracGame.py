class DiracGame:

    def __init__(self,starting_positions) -> None:
        self.die_values = 3
        self.die_rolls_per_turn = 3
        self.multiplier = self.die_values ** self.die_rolls_per_turn
        self.no_players = 2
        self.players = [DiracPlayer() for _ in range(self.no_players)]
        for i in range(self.no_players):
            self.players[i].set_start_position(starting_positions[i])
        self.active_player = 0

    def determine_winner(self) -> int:
        winning_score = 0
        for player in self.players:
            winning_score = max(winning_score, player.wins)
        return int(winning_score)

    def play_full_game(self) -> int:
        while self.players[0].active_pawns() > 0 and self.players[1].active_pawns() > 0:
            self.take_turn()
        return self.determine_winner()

    def next_player(self) -> None:
        player_id = self.active_player
        player_id += 1
        if player_id > 1:
            player_id = 0
        self.active_player = player_id
        
    def update_non_active_player(self, losers: int) -> None:
        inactive_player = 0
        if self.active_player == 0:
            inactive_player = 1
        self.players[inactive_player].multiply_all(self.multiplier)
        if losers > 0:
            self.players[inactive_player].remove_losers(losers)

    def take_turn(self) -> None:
        winning_pawns = self.players[self.active_player].move_all_pawns()
        self.update_non_active_player(winning_pawns)
        self.next_player()
        
class DiracPlayer:

    def __init__(self) -> None:
        self.board_spaces = 10
        self.target_score = 21
        self.pawns = self.new_blank_grid()
        self.wins = 0

    def new_blank_grid(self) -> list:
        grid = [[0] * (self.board_spaces+1) for _ in range(self.target_score + self.board_spaces)]
        return grid

    def set_start_position(self, starting_position: int) -> None:
        self.pawns[0][starting_position] = 1

    def active_pawns(self) -> int:
        total_pawns = 0
        for score in range(0,21):
            total_pawns += sum(self.pawns[score])
        return total_pawns

    def handle_winning_pawns(self) -> int:
        winners = 0
        for score in range(21,31):
            for place in range(1,11):
                winners += self.pawns[score][place]
                self.pawns[score][place] = 0
        self.wins += winners
        return winners
    
    def remove_losers(self, losers: int) -> None:
        total_pawns = self.active_pawns()
        remainers = total_pawns - losers
        for i in range(len(self.pawns)):
            for j in range(len(self.pawns[0])):
                no_pawns = self.pawns[i][j]
                no_pawns *= remainers
                no_pawns /= total_pawns
                self.pawns[i][j] = no_pawns

    def multiply_all(self, multiplier) -> None:
        for i in range(len(self.pawns)):
            for j in range(len(self.pawns[0])):
                self.pawns[i][j] *= multiplier
    
    def move_pawn_group(self, place, current_score, new_pawn_locations) -> None:
        distribution = [0,0,0,1,3,6,7,6,3,1] #Probability ditribution of die results
        no_pawns = self.pawns[current_score][place]
        for this_roll in range(3,10): #valid roles are 3,4,5,6,7,8,9
            new_place = place + this_roll
            if new_place > 10:
                new_place -= 10
            new_score = new_place + current_score
            new_pawn_locations[new_score][new_place] += no_pawns * distribution[this_roll]

    def move_pawns_with_score(self, score, new_pawn_locations) -> None:
        for place in range(1,11):
            self.move_pawn_group(place, score, new_pawn_locations)

    def move_all_pawns(self) -> int:
        new_pawn_locations = self.new_blank_grid()
        for score in range(0,21): #Only move pawns that haven't won yet
            self.move_pawns_with_score(score, new_pawn_locations)
        self.pawns = new_pawn_locations
        return self.handle_winning_pawns()