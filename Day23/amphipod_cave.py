from typing import List, Tuple, Set
from amphipod import Amphipod


class AmphipodCave:
    """Representation of a Cave full of Amphipods"""

    HALL_STOP_POINTS = {(1, 1), (2, 1), (4, 1), (6, 1), (8, 1), (10, 1), (11, 1)}
    ROOMS = {
        "A": [(3, 2), (3, 3), (3, 4), (3, 5)],
        "B": [(5, 2), (5, 3), (5, 4), (5, 5)],
        "C": [(7, 2), (7, 3), (7, 4), (7, 5)],
        "D": [(9, 2), (9, 3), (9, 4), (9, 5)],
    }

    def __init__(self) -> None:
        self.pods = []
        self.no_pods = 0
        self.complete = False
        self.map = {(1,1): None, (2,1): None, (3,1): None, (4,1): None, (5,1): None, (6,1):None, (7,1):None, (8,1): None, (9,1): None, (10,1): None, (11,1): None}
        for room in AmphipodCave.ROOMS.values():
            for location in room:
                self.map.update({location: None})



    
        

    def place_new_amphipod(self, colour: str, location: Tuple[int, int]) -> None:
        """Creates a new Amphipod and positions it in the correct place"""
        self.pods.append(Amphipod(colour, location))
        self.set_pod_status(self.pods[-1])
        self.no_pods = len(self.pods)

    def confirm_pod_colour_at_location(self, location: Tuple[int, int]) -> str | None:
        """Check the colour of pod at a given location"""
        for pod in self.pods:
            if pod.positions[-1] == location:
                return pod.colour
        return None

    def set_pod_status(self, amphipod: Amphipod) -> None:
        """Checks to see if pod in question is already in its final position"""
        my_colour = amphipod.colour
        my_room = AmphipodCave.ROOMS[my_colour]
        position = amphipod.positions[-1]
        if position not in my_room:
            amphipod.done = False
        elif position == my_room[-1]:
            amphipod.done = True
        elif position == my_room[-2]:
            if self.confirm_pod_colour_at_location(my_room[-1]) == my_colour:
                amphipod.done = True
        elif position == my_room[-3]:
            if (
                self.confirm_pod_colour_at_location(my_room[-1]) == my_colour
                and self.confirm_pod_colour_at_location(my_room[-2]) == my_colour
            ):
                amphipod.done = True
        elif position == my_room[-4]:
            if (
                self.confirm_pod_colour_at_location(my_room[-1]) == my_colour
                and self.confirm_pod_colour_at_location(my_room[-2]) == my_colour
                and self.confirm_pod_colour_at_location(my_room[-3]) == my_colour
            ):
                amphipod.done = True
        else:
            amphipod.done = False

    def valid_next_positions(self, amphipod: Amphipod) -> List[Tuple[int, int]]:
        """Return list of positions amphipod could move to next"""
        current_position = amphipod.positions[-1]
        colour = amphipod.colour

        if amphipod.done is True:
            return []

        if current_position in AmphipodCave.HALL_STOP_POINTS:
            return AmphipodCave.ROOMS[colour]

        valid_next_positions = list(AmphipodCave.HALL_STOP_POINTS)
        valid_next_positions.extend(AmphipodCave.ROOMS[colour])
        if current_position in valid_next_positions:
            valid_next_positions.remove(current_position)
        return list(valid_next_positions)

    def get_path(
        self, start: Tuple[int, int], end: Tuple[int, int]
    ) -> Set[Tuple[int, int]]:
    """Returns all positions traversed between start and end, including end, excluding start"""
        start_x, start_y = start
        end_x, end_y = end

        path = {end}

        if start_x < end_x:
            for x in range(start_x, end_x + 1):
                path.add((x, 1))
        else:
            for x in range(end_x, start_x + 1):
                path.add((x, 1))

        if start_y > 1:
            for y in range(2, start_y):
                path.add((start_x, y))

        if end_y > 1:
            for y in range(2, end_y):
                path.add((end_x, y))

        path.discard(start)
        return path

    def pod_locations(self) -> Set[Tuple[int, int]]:
        """Return locations of all pods"""
        locations = set()
        for pod in self.pods:
            locations.add(pod.positions[-1])
        return locations

    def reachable(self, amphipod: Amphipod, destination: Tuple[int, int]) -> bool:
        """Return True is destination is reachable by amphipod"""
        path = self.get_path(amphipod.positions[-1], destination)
        pod_locations = self.pod_locations()

        if path.intersection(pod_locations) == set():
            return True
        return False

    def prioritise_move_list(
        self, moves: List[Tuple[Amphipod, Tuple[int, int]]]
    ) -> List[Tuple[Amphipod, Tuple[int, int]]]:
    """ Prioritise Move list for efficiency of search"""
        possible_moves = set(moves)
        prioritised_moves = []

        #Priority 1 - Moves to home position
        for move in moves:
            pod, location = move
            if location in AmphipodCave.ROOMS[pod.colour]:
                prioritised_moves.append(move)
                possible_moves.remove(move)
        #Priority 2 - Everything else
        for move in possible_moves:
            prioritised_moves.append(move)
        
        return prioritised_moves
            
    def next_moves(self) -> List[Tuple[Amphipod, Tuple[int, int]]]:
        """Returns a list of possible next moves"""
        moves = []
        for pod in self.pods:
            if pod.done is False:
                destinations = self.valid_next_positions(pod)

            for location in destinations:
                if self.reachable(pod, location) is True:
                    moves.append((pod, location))

        moves = self.prioritise_move_list(moves)
        return moves

    def do_move(self, pod: Amphipod, location: Tuple[int, int]):
        """Carry out move"""
        cost = self.calculate_move_cost(pod, location)
        pod.positions.append(location)
        return cost

    def calculate_move_cost(
        self, amphipod: Amphipod, destination: Tuple[int, int]
    ) -> int:
        """Returns the cost of moving an Amphipod to a given location"""
        current_x, current_y = amphipod.positions[-1]
        dest_x, dest_y = destination

        cost = 0

        cost += abs(dest_x - current_x)
        cost += current_y - 1
        cost += dest_y - 1

        return cost
