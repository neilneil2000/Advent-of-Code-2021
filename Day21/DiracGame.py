class DiracGame:

    def __init__(self,starting_positions):
        self.multiplier = 3 * 3 * 3
        self.players = 2
        self.player_grids = [DiracGridManager() for _ in range(self.players)]
        self.winning_universes = [0,0]
        self.active_player = 0
        p1_grid = self.player_grids[0].grid.grid
        p2_grid = self.player_grids[1].grid.grid
        p1_start, p2_start = starting_positions
        p1_grid[0][p1_start] = 1
        p2_grid[0][p2_start] = 1


    def play_full_game(self):
        while self.player_grids[0].active_pawns() > 0 and self.player_grids[1].active_pawns() > 0:
            self.take_turn()

    def next_player(self):
        player_id = self.active_player
        player_id += 1
        if player_id > 1:
            player_id = 0
        self.active_player = player_id

    def move_pawns(self):
        player = self.active_player
        return self.player_grids[player].move_all_pawns()    
        
    def update_non_active_player(self, losers: int):
        inactive_player = 0
        if self.active_player == 0:
            inactive_player = 1
        self.player_grids[inactive_player].multiply_all()
        if losers > 0:
            self.player_grids[inactive_player].remove_losers(losers)

    def take_turn(self):
        winners_this_round = self.move_pawns()
        self.winning_universes[self.active_player] += winners_this_round
        self.update_non_active_player(winners_this_round)
        self.next_player()
        
class DiracGridManager:

    def __init__(self):
        self.grid = DiracGrid(10,21)
        self.next_grid = DiracGrid(10,21)

    def remove_losers(self, losers: int) -> None:
        self.grid.remove_losers(losers)

    def active_pawns(self) -> int:
        return self.grid.active_pawns()

    def handle_winning_pawns(self) -> int:
        winners = 0
        for score in range(21,31):
            for place in range(1,11):
                winners += self.grid.grid[score][place]
                self.grid.grid[score][place] = 0
        return winners

    def multiply_all(self):
        self.grid.multiply_all(27)
    
    def move_pawn_group(self, place, current_score):
        distribution = [0,0,0,1,3,6,7,6,3,1] #Probability ditribution of die results
        no_pawns = self.grid.grid[current_score][place]
        for this_roll in range(3,10): #valid roles are 3,4,5,6,7,8,9
            new_place = place + this_roll
            if new_place > 10:
                new_place -= 10
            new_score = new_place + current_score
            self.next_grid.grid[new_score][new_place] += no_pawns * distribution[this_roll]

    def move_pawns_with_score(self, score):
        for place in range(1,11):
            self.move_pawn_group(place, score)

    def move_all_pawns(self) -> int:
        for score in range(0,21): #Only move pawns that haven't won yet
            self.move_pawns_with_score(score)
        self.grid = self.next_grid
        self.next_grid = DiracGrid(10,21)
        return self.handle_winning_pawns()
                
class DiracGrid:

    def __init__(self,board_spaces, target_score):
        self.grid = [[0] * (board_spaces+1) for _ in range(target_score + board_spaces)]

    def active_pawns(self) -> int:
        total_pawns = 0
        for score in range(0,21):
            total_pawns += sum(self.grid[score])
        return total_pawns

    def remove_losers(self, losers: int) -> None:
        total_pawns = self.active_pawns()
        remainers = total_pawns - losers
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                pawns = self.grid[i][j]
                pawns *= remainers
                pawns /= total_pawns
                self.grid[i][j] = pawns


    def multiply_all(self, multiplier):
        for i in range(len(self.grid)):
            for j in range(len(self.grid[0])):
                self.grid[i][j] *= multiplier
