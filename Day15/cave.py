from os import get_inheritable


class Cave:

    def __init__(self,filename):
        self.lowest_path = 99999999999999999 #arbitrarily high
        self.read_input_file(filename)
        self.width = len(self.cave_risk[0])
        self.height = len(self.cave_risk)

    def compute_path(self):
        current_location = (0,0)
        neighbours = self.get_neighbours(current_location)
        for neighbour in neighbours:
            self.next_step(current_location,neighbour,0)

    def get_neighbours(self,location) -> list:
        neighbours = []
        x, y = location
        
        if x < self.width - 1:
            neighbours.append((x + 1, y))
        if y < self.height - 1:
            neighbours.append((x, y + 1))
        if x > 0:
            neighbours.append((x - 1, y))
        if y > 0:
            neighbours.append((x, y - 1))
        
        return neighbours


    def next_step(self, from_location: tuple, location: tuple, path_risk: int) -> None:
        x, y = location
        path_risk += self.cave_risk[y][x]
        if path_risk >= self.lowest_path:
            return
        if location == (self.width - 1, self.height - 1):
            self.lowest_path = path_risk
            print(f'Better Path Found. Value: {path_risk}')
            return
        neighbours = self.get_neighbours(location)
        neighbours.remove(from_location)
        for neighbour in neighbours:
            self.next_step(location,neighbour,path_risk)



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