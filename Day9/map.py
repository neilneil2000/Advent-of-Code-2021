class Map:

    def __init__(self,filename):
        self.topology = []
        self.low_points = set()
        self.risk_value = 0
        self.read_input_file(filename)
        print(self.topology)


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
                    print(f'Low point found. Height: {self.topology[i][j]} Location {i},{j}')

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
