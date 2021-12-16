from time import time


class Cave:

    def __init__(self,filename):
        self.lowest_path = 99999999999999999 #arbitrarily high
        self.read_input_file(filename)
        self.cave_risk[0][0] = 0
        self.width = len(self.cave_risk[0])
        self.height = len(self.cave_risk)
        self.cave_cumulative_risk = []
        empty_row = [None] * self.width
        for _ in range(0,self.height):
            self.cave_cumulative_risk.append(empty_row.copy())
        self.cave_cumulative_risk[self.height - 1][self.width - 1] = self.cave_risk[self.height - 1][self.width - 1]

    def get_best(self, location, neighbour_target, from_location):
        """
        Tries to get to the end in a lower number of steps than {max}
        Returns the number of steps if it can beat it
        Returns None if it can't
        """
        x, y = location
        path_found = False

        known_best = self.cave_cumulative_risk[y][x]
        if known_best is not None:
            if known_best < neighbour_target:         
                return known_best #If I know the answer, tell them
            else:
                return None
        
        my_risk = self.cave_risk[y][x]
        neighbour_target -= my_risk
        if neighbour_target <= 0:
            return None #Can't beat it coming through me
        
        neighbours = self.get_neighbours(location)
        if from_location in neighbours:
            neighbours.remove(from_location) #Don't go back on yourself

        for neighbour in neighbours:
            n = self.get_best(neighbour, neighbour_target, location)
            if n is not None:
                neighbour_target = min(neighbour_target, n)
                path_found = True

        if path_found == True:
            my_best = neighbour_target + my_risk
            self.cave_cumulative_risk[y][x] = my_best
            print(f'{time()}: Value at Location ({x},{y}) confirmed as {my_best}')
            return my_best
        else:
            return None




    def get_neighbours(self,location) -> list:
        neighbours = []
        x, y = location
        
        if x < self.width - 1:
            neighbours.append((x + 1, y)) #Look Right
        if y < self.height - 1:
            neighbours.append((x, y + 1)) #Look Down
        if x > 0:
            neighbours.append((x - 1, y)) #Look Left
        if y > 0:
            neighbours.append((x, y - 1)) #Look Up
        
        return neighbours



    def read_input_file(self,filename):
        input = []
        with open(filename,'r') as f:
            for line in f:
                input.append(list(line.strip()))
        self.width = len(input[0])
        self.height = len(input)
        for i, row in enumerate(input):
            for j, _ in enumerate(row):
                input[i][j] = int(input[i][j])
        self.cave_risk = input