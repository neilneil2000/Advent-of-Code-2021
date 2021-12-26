class Grid:

    def __init__(self, grid_data):
        self.floor = grid_data

    def print_floor(self):
        for row in self.floor:
            print(''.join(row))
        print()

    def move_until_static(self):
        rounds = 0
        moves = 1
        while moves > 0:
            moves = self.move_both_herds()
            rounds += 1
        return rounds

    def move_both_herds(self):
        """Moves both herds and returns total number of moves across both"""
        moves_this_round = 0
        moves_this_round += self.move('>')
        moves_this_round += self.move('v')
        return moves_this_round

    def move(self, herd: str) -> int:
        """Executes moves for a herd and returns total number of moves executed"""
        x_inc = 0
        y_inc = 0
        no_moves = 0
        moveable = self.get_moves()
        if herd == 'v':
            y_inc += 1
        elif herd == '>':
            x_inc += 1
        for y, row in enumerate(moveable):
            for x, square in enumerate(row):
                if self.floor[y][x] == herd and square == True:
                    self.floor[y][x] = '.'
                    no_moves += 1
                    if y + y_inc >= len(self.floor):
                        self.floor[0][x] = herd
                    elif x + x_inc >= len(self.floor[0]):
                        self.floor[y][0] = herd
                    else:
                        self.floor[y + y_inc][x + x_inc] = herd
        return no_moves


    def get_moves(self):
        moveable = []
        for y, row in enumerate(self.floor):
            moveable_row = []
            for x, _ in enumerate(row):
                moveable_row.append(self.can_i_move((x,y)))
            moveable.append(moveable_row)
        return moveable

    def can_i_move(self, location):
        """Takes current location and confirms whether or not you can move this turn"""
        x, y = location
        herd = self.floor[y][x]
        if herd == '.':
            return False #Empty Space
        if herd == 'v':
            if y >= len(self.floor) -1:
                y = 0
            else:
                y += 1
        else:
            if x >= len(self.floor[0]) -1:
                x = 0
            else:
                x += 1
        if self.floor[y][x] == '.':
            return True
        return False
         
