class FoldablePaper:
    
    def __init__(self,filename):
        self.points = set()
        self.folds = []
        self.read_input_file(filename)
        self.folds_complete = 0
        
    def execute_next_fold(self):
        fold_line = self.folds[self.folds_complete]
        new_points = set()
        for point in self.points:
            new_point = ()
            if fold_line[0] == 'y':
                if point[1] > fold_line[1]:
                    new_point = (point[0], 2*fold_line[1] - point[1])
                else: 
                    new_point = point
            else:
                if point[0] > fold_line[1]:
                    new_point = (2*fold_line[1] - point[0], point[1])
                else:
                    new_point = point
            #print(f'{point} becomes {new_point}')
            new_points.add(new_point)
        self.points = new_points
        self.folds_complete += 1
    
    def read_input_file(self,filename):
        with open(filename,'r') as f:
            for line in f:
                line = line.strip()
                if line == '':
                    pass
                elif line[0] == 'f':
                    line = line.split(' ')
                    fold = line[2].split('=')
                    self.folds.append((fold[0],int(fold[1])))
                else:
                    point = line.split(',')
                    point  = (int(point[0]),int(point[1]))
                    self.points.add(point)
        print(f'{len(self.points)} points and {len(self.folds)} folds loaded')
