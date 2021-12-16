from time import time
from sys import setrecursionlimit


class Cave:

    def __init__(self,filename):
        setrecursionlimit(1000000)
        self.lowest_path = 99999999999999999 #arbitrarily high
        self.read_input_file(filename)
        self.create_mega_map()
        self.cave_risk[0][0] = 0
        self.width = len(self.cave_risk[0])
        self.height = len(self.cave_risk)
        self.cave_cumulative_risk = []
        self.cave_at_least_risk = []
        empty_row = [None] * self.width
        for _ in range(0, self.height):
            self.cave_cumulative_risk.append(empty_row.copy())
        for i in range(0, self.height):
            self.cave_at_least_risk.append(self.cave_risk[i].copy())

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

        if neighbour_target <= self.cave_at_least_risk[y][x]:
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
            #print(f'{time()}: Value at Location ({x},{y}) confirmed as {my_best}')
            return my_best
        else:
            self.cave_at_least_risk[y][x] = max(self.cave_at_least_risk[y][x],neighbour_target + my_risk)
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

    def print_map(self):
        for row in self.cave_risk:
            for item in row:
                print(f'{item}',end='')
            print()


    def create_mega_map(self):
        #Make it mega wide
        for y in range(0,self.height):
            row_pointer = self.cave_risk[y].copy()
            for _ in range(0,4):
                self.cave_risk[y].extend(row_pointer.copy())
        #Make it mega tall
        for _ in range(0,4):
            for y in range(0,self.height):
                self.cave_risk.append(self.cave_risk[y].copy())
        
        #Set Correct Values
        for y,row in enumerate(self.cave_risk):
            for x,_ in enumerate(row):
                inc = int(x / self.width) + int(y / self.height)                
                self.cave_risk[y][x] += inc
                if self.cave_risk[y][x] > 9:
                    self.cave_risk[y][x] -= 9

        #Reset Height & Width Parameters
        self.height = len(self.cave_risk)
        self.width = len(self.cave_risk[0])


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