from enum import Enum

class Rules:
    no_rules = 0
    transit_only = 1
    amber_only = 3
    bronze_only = 4
    copper_only = 5
    dessert_only = 6


class Amphipod:
    
    Halls = { 'A': 3,
    'B' : 5,
    'C' : 7,
    'D' : 9}

    Costs = { 'A' :1,
    'B' : 10,
    'C' : 100,
    'D' : 1000
    }

    def __init__(self, colour, position):
        self.colour = colour
        self.position = position
        self.cost = Amphipod.Costs[colour]

class AmphipodGrid:

    location_rules = {
        (0, 0) : Rules.no_rules,
        (1, 0) : Rules.no_rules,
        (2, 0) : Rules.transit_only,
        (2, 1) : Rules.amber_only,
        (2, 2) : Rules.amber_only,
        (2, 3) : Rules.amber_only,
        (2, 4) : Rules.amber_only,
        (3, 0) : Rules.no_rules,
        (4, 0) : Rules.transit_only,
        (4, 1) : Rules.bronze_only,
        (4, 2) : Rules.bronze_only,
        (4, 3) : Rules.bronze_only,
        (4, 4) : Rules.bronze_only,
        (5, 0) : Rules.no_rules,
        (6, 0) : Rules.transit_only,
        (6, 1) : Rules.copper_only,
        (6, 2) : Rules.copper_only,
        (6, 3) : Rules.copper_only,
        (6, 4) : Rules.copper_only,
        (7, 0) : Rules.no_rules,
        (8, 0) : Rules.transit_only,
        (8, 1) : Rules.dessert_only,
        (8, 2) : Rules.dessert_only,
        (8, 3) : Rules.dessert_only,
        (8, 4) : Rules.dessert_only,
        (9, 0) : Rules.no_rules,
        (10,0) : Rules.no_rules
    }

    def __init__(self, filename):
        warren_data = self.read_input_file(filename)
        self.amphipods = []
        self.location_occupancy = {}
        self.setup_warren(warren_data)
        self.transit_only = self.get_transit_only_spaces()
        self.get_legal_moves()

    def get_transit_only_spaces(self):
        """Manual Hack for now - later check if has >2 neighbours"""
        return {(3,1),(5,1),(7,1),(9,1)}
        

    def setup_warren(self,warren_data):
        occupancy = {}
        for y, row in enumerate(warren_data):
            for x, contents in enumerate(row):
                if contents in {' ','#'}:
                    pass
                elif contents == '.':
                    occupancy.update( { (x, y) : False } )
                else:
                    self.amphipods.append(Amphipod(contents,(x,y)))
                    occupancy.update( { (x, y) : True})

        self.location_occupancy = occupancy

    def get_empty_squares(self) -> set:
        empty_squares = set()
        for location, status in self.location_occupancy.items():
            if status == False:
                empty_squares.add(location)
        return empty_squares

    def get_legal_moves(self):
        end_points = self.get_empty_squares()
        for square in self.transit_only:
            end_points.discard(square)
        
        #Get Customised List per amphipod
        for amphipod in self.amphipods:
            my_end_points = end_points.copy()
            for square in end_points:
                x,y = square
                if y > 1:   #Remove rooms for other colours
                    if amphipod.colour == 'A':
                        if x != 3:
                            my_end_points.discard(square)
                    elif amphipod.colour == 'B':
                        if x != 5:
                            my_end_points.discard(square)
                    elif amphipod.colour == 'C':
                        if x != 7:
                            my_end_points.discard(square)
                    elif amphipod.colour == 'D':
                        if x != 9:
                            my_end_points.discard(square)
            #Remove own hall if contains a non-correct colour
            #remove all but bottom of call
                

            print(amphipod.colour)




       
        
    def read_input_file(self, filename):
        raw_data =[]
        with open(filename, 'r') as f:
            for line in f:
                raw_data.append(line.strip('\n'))
        return raw_data

   