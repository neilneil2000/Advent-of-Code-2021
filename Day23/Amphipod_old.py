from enum import Enum
import time

class Rules(Enum):
    no_rules = 0
    transit_only = 1
    amber_only = 3
    bronze_only = 4
    copper_only = 5
    dessert_only = 6

class Amphipod:
    
    COSTS = { 'A' :1,
              'B' : 10,
              'C' : 100,
              'D' : 1000 }

    def __init__(self, colour, position):
        self.colour = colour
        self.positions = []
        self.positions.append(position)
        self.position = self.positions[-1]
        self.cost = Amphipod.COSTS[colour]
        self.done = False #True when in final position

    def rewind(self):
        """Step back (used when going back through recursive solution finder)"""
        previous_position = self.positions.pop()
        self.position = self.positions[-1]
        self.done = False
        return previous_position

    def move(self, end: tuple) -> int:
        """Move to new position and return cost of doing so"""
        start_x, start_y = self.position
        end_x, end_y = end

        space_counter  = abs(start_x - end_x) # Horizontal move
        space_counter += start_y - 1
        space_counter += end_y - 1

        self.positions.append(end)
        if len(self.positions) > 3:
            print(f'ERROR TOO MANY MOVES')
        self.position = self.positions[-1]
        return space_counter * self.cost

class AmphipodGrid:

    ROOMS = {   'A' : { (3,2), (3,3), (3,4), (3,5) },
                'B' : { (5,2), (5,3), (5,4), (5,5) },
                'C' : { (7,2), (7,3), (7,4), (7,5) },
                'D' : { (9,2), (9,3), (9,4), (9,5) },
                'All': { (3,2), (3,3), (3,4), (3,5), (5,2), (5,3), (5,4), (5,5), (7,2), (7,3), (7,4), (7,5), (9,2), (9,3), (9,4), (9,5) }}
                #'All': { (3,2), (3,3), (5,2), (5,3), (7,2), (7,3), (9,2), (9,3) }}

    HALL_STOP_POINTS = { (1,1), (2,1), (4,1), (6,1), (8,1), (10,1), (11,1) }
        

    def __init__(self, filename):
        self.room_status = { 'A' : False,
                            'B' : False,
                            'C' : False,
                            'D' : False } #Is hall ready to accept incoming Amphipods? (i.e. is it empty or only contains correct Amphipods)
        self.game_complete = False
        self.winning_score  = 0
        warren_data = self.read_input_file(filename)
        self.amphipods = []
        self.location_occupancy = {}
        self.setup_warren(warren_data)
        self.check_rooms()
        self.is_complete()

    def min_score_from_here(self):
        """Returns a rough minimum score from here, always lower than reality"""
        total = 0
        for pod in self.amphipods:
            x,y = pod.position
            colour = pod.colour
            cost = Amphipod.COSTS[colour]
            if pod.position not in AmphipodGrid.ROOMS[colour]:
                if colour == 'A':
                    target = (3,2)
                elif colour == 'B':
                    target = (5,2)
                elif colour == 'C':
                    target = (7,2)
                elif colour == 'D':
                    target = (9,2)
                target_x, target_y = target

                total += abs(x - target_x) * cost # Horizontal move
                total += (target_y - 1) * cost
                total += (target_y - 1) * cost
        return total


    def compute_best_score(self):
        moves = self.get_possible_moves()
    
        best_cost = 99999999999999
        for move in moves:
            print(f'*****************************************************')
            print(f'   Attempting {move[0].colour} : {move[0].position}  -> {move[1]} as first move  ')
            print(f'*****************************************************')
            pod, location  = move
            start_time = time.perf_counter()
            solution_cost = (self.move_manager(pod, location, 0, best_cost))
            end_time = time.perf_counter()
            prev = pod.rewind()
            if prev != location:
                print(f"It's Gone Wrong!")
            self.location_occupancy[pod.position] = True
            self.location_occupancy[prev] = False
            best_cost = min(best_cost, solution_cost)
            print(f'Execution Time : {end_time - start_time:0.6f}')
            print(f'Best so far: {solution_cost}')
            print()
                
        self.winning_score = best_cost
                
        print(f'Winning score is: {self.winning_score}')

    def is_complete(self) -> bool:
        """Checks Amphipod locations and updates self.game_complete"""
        for pod in self.amphipods:
            if pod.position not in AmphipodGrid.ROOMS[pod.colour]:
                return False
        #self.game_complete = True
        return True
    
    def check_rooms(self) -> None:
        """Update hall status to see if they are ready to accept incoming Amphipods"""
        Readiness = { 'A' : True, 'B' : True, 'C' : True, 'D' : True }
        for pod in self.amphipods:
            position = pod.position
            if position not in AmphipodGrid.ROOMS[pod.colour]:
                if position in AmphipodGrid.ROOMS['A']:
                    Readiness.update({ 'A': False })
                elif position in AmphipodGrid.ROOMS['B']: 
                    Readiness.update({ 'B': False })
                elif position in AmphipodGrid.ROOMS['C']: 
                    Readiness.update({ 'C': False })
                elif position in AmphipodGrid.ROOMS['D']:
                    Readiness.update({ 'D': False })
        for hall in Readiness:
            self.room_status[hall] = Readiness[hall] 

    def move(self, amphipod: Amphipod, location: tuple):
        cost = amphipod.move(location)
        if amphipod.position in AmphipodGrid.ROOMS[amphipod.colour] and \
            self.room_status[amphipod.colour] == True:
            amphipod.done = True
        #Set done if appropriate
        return cost

    def move_manager(self, amphipod: Amphipod, location: tuple, total_cost: int, best_cost: int) -> int:
        """Move Amphipod to new location and add cost to total"""
        previous_location = amphipod.position
        total_cost += self.move(amphipod, location) #Do move and add cost to total
        self.location_occupancy[location] = True
        self.location_occupancy[previous_location] = False
        if total_cost >= best_cost:
            return total_cost #Don't bother going further than the best solution so far
        if self.min_score_from_here() + total_cost > best_cost:
            return best_cost #No routes from here can beat the best
        if self.is_complete() == True:
            print(f'{total_cost}: New Best Solution Found')
            return total_cost # Return total cost for solution
        
        moves = self.get_possible_moves()
        self.check_rooms()
        for move in moves:
            pod, move_location = move
            #Only attempt if not in home space
            if pod.done == False:
                solution_cost = self.move_manager(pod, move_location, total_cost, best_cost)
                prev = pod.rewind()
                if prev != move_location:
                    print(f"It's Gone Wrong!")
                self.location_occupancy[pod.position] = True
                self.location_occupancy[prev] = False
                best_cost = min(best_cost, solution_cost)
        return best_cost

    def get_possible_moves(self) -> list:
        """Returns list of all possible moves. Each list entry is (Amphipod, destination:tuple)"""
        #For each Amphipod work out next legal moves
        moves = []
        for amphipod in self.amphipods:
            if amphipod.done == False:
                end_points = self.get_legal_endpoints(amphipod)
                reachables = self.get_reachable_points(amphipod.position, amphipod.position, set())
                end_points.intersection_update(reachables)
                pass
                for location in end_points:
                    moves.append((amphipod, location))

        return moves

    def get_reachable_points(self, position: tuple, from_position: tuple, reachable_so_far: set) -> set:
        """Get squares that are reachable from *position*"""
        if position not in self.location_occupancy:
            return reachable_so_far # We've hit a wall
        if self.location_occupancy[position] == True and position != from_position:
            return reachable_so_far # We've hit another player
        else:
            x,y = position
            neighbours = {(x+1, y),(x-1, y),(x, y+1),(x, y-1)}
            neighbours.discard(from_position)
            for neighbour in neighbours:
                neighbour_points = self.get_reachable_points(neighbour, position, reachable_so_far)
                reachable_so_far = reachable_so_far.union(neighbour_points)
        if position != from_position:
            reachable_so_far.add(position) #This is a legal position
        return reachable_so_far

    def get_legal_endpoints(self, amphipod) -> set:
        self.check_rooms()
        position = amphipod.position
        end_points = set()

        if self.room_status[amphipod.colour]:
            if position in AmphipodGrid.ROOMS[amphipod.colour]:
                return end_points #I'm already in a home spot so no moves sensible from here - return empty set
            else: #Add lowest free spot in room
                room_spaces = AmphipodGrid.ROOMS[amphipod.colour].copy()
                free_room_spaces = set()
                for space in room_spaces:
                    if self.location_occupancy[space] == False:
                        free_room_spaces.add(space)
                if len(free_room_spaces) > 1:
                    y_max = 0
                    for space in free_room_spaces:
                        x,y = space
                        y_max = max(y, y_max)
                    free_room_spaces = {(x,y_max)}
                end_points = end_points.union(free_room_spaces)

        if position in AmphipodGrid.ROOMS['All']:
            end_points = end_points.union(AmphipodGrid.HALL_STOP_POINTS) #If I'm in a room I can stop at hall stop points      

        return end_points

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

    def read_input_file(self, filename):
        raw_data =[]
        with open(filename, 'r') as f:
            for line in f:
                raw_data.append(line.strip('\n'))
        return raw_data

   