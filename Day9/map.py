class Map:

    def __init__(self,filename):
        self.topology = []
        self.low_points = set()
        self.risk_value = 0
        self.read_input_file(filename)
        self.length = len(self.topology)
        self.width = len(self.topology[0])
        self.basin_id = 0 #Tracks largest marked basin
        self.basin_sizes = []


    def read_input_file(self,filename):
        with open(filename,'r') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                line = list(line.strip())
                for i,v in enumerate(line):
                    line[i] = int(line[i])
                self.topology.append(line)

    def calculate_basin_sizes(self):
        for x in range(0,self.basin_id):
            counter = 0
            for row in self.basin_map:
                for basin_value in row:
                    if basin_value == x:
                        counter += 1
            self.basin_sizes.append(counter)


    def assign_to_basin(self,row,column,basin_id):
        if self.basin_map[row][column] is not None:
            return False
        if self.topology[row][column] >= 9:
            return False
        self.basin_map[row][column] = basin_id
        if row > 0:
            self.assign_to_basin(row - 1, column, basin_id)
        if row < self.length - 1:
            self.assign_to_basin(row + 1, column, basin_id)
        if column > 0:
            self.assign_to_basin(row, column - 1, basin_id)
        if column < self.width - 1:
            self.assign_to_basin(row, column + 1, basin_id)
        return True

    def sort_basin_sizes(self):
        self.basin_sizes.sort()

    def mark_basins(self):
        basin_row = [None] * len(self.topology[0])
        self.basin_map = []
        for x in self.topology:
            self.basin_map.append(basin_row.copy())
        for row_id,row in enumerate(self.topology):
            for column_id,height in enumerate(self.topology[row_id]):
                if self.assign_to_basin(row_id,column_id,self.basin_id):
                    self.basin_id += 1


    def calculate_risk(self):
        self.risk_value += len(self.low_points)
        for point in self.low_points:
            self.risk_value += self.topology[point[0]][point[1]]
        return self.risk_value

    def find_low_points(self):
        for i,v, in enumerate(self.topology):
            for j,w in enumerate(self.topology[i]):
                if self.is_low_point(i,j):
                    self.low_points.add((i,j))
                    #print(f'Low point found. Height: {self.topology[i][j]} Location {i},{j}')

    def is_low_point(self,i,j):
        height = self.topology[i][j]
        surrounding = set()
        if i > 0:
            surrounding.add(self.topology[i-1][j])
        if i < (len(self.topology)-1):
            surrounding.add(self.topology[i+1][j])
        if j > 0:
            surrounding.add(self.topology[i][j-1])
        if j < (len(self.topology[i])-1):
                surrounding.add(self.topology[i][j+1])
        #print(f'{height} surrounded by {surrounding}')
        for neighbour_height in surrounding:
            if height >= neighbour_height:
                #print("Not a low point")
                return False
        #print("LOW Point")
        return True
