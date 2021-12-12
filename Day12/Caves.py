from Path import Path
import copy

class Caves:

    def __init__(self,filename):
        self.links = {}
        self.small_caves = set()
        self.paths = set()
        self.read_input_file(filename)
    
    def print_paths(self):
        for path in self.paths:
            path.print_path()
        print(f'{len(self.paths)} paths found')
        

    def add_next_step(self,path): # This is the recursive function that keeps adding steps until it reaches end
        #get possible next steps
        #pick next step; add to steps and remove from dictionary if small
        if path.steps[-1] == 'end':
            return True
        next_steps = path.get_valid_next_steps()
        for step in next_steps:
            new_path = copy.deepcopy(path)
            new_path.confirm_next_step(step)
            if self.add_next_step(new_path):
                self.paths.add(new_path)
        del path
        

    def build_path(self): #This is the point from which all new paths are created
        path = Path(self.links)
        if self.add_next_step(path):
            self.paths.add(path)



    def compute_paths(self):
        self.build_path()
        

    def read_input_file(self,filename):
        with open(filename,'r') as f:
            for line in f:
                line = line.strip()
                link = line.split('-')
                self.add_link(link)
    
    def add_link_directional(self,start,end):
        if start == 'end' or end == 'start':
            return
        if start.lower() == start:
            self.small_caves.add(start)
        if end.lower() == end:
            self.small_caves.add(end)
        linked_set = self.links.get(start)
        if linked_set is None:
            linked_set = set()
        linked_set.add(end)
        self.links.update({start:linked_set})

    def add_link(self,link):
        self.add_link_directional(link[0],link[1])
        self.add_link_directional(link[1],link[0])
