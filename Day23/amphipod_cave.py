from typing import Tuple, Dict, List, Set
from logging import Logger
from time import perf_counter


class AmphipodCave:
    """Representation of a Cave full of Amphipods"""

    HALL_STOP_POINTS = {(1, 1), (2, 1), (4, 1), (6, 1), (8, 1), (10, 1), (11, 1)}
    ROOMS = {
        "A": [(3, 2), (3, 3), (3, 4), (3, 5)],
        "B": [(5, 2), (5, 3), (5, 4), (5, 5)],
        "C": [(7, 2), (7, 3), (7, 4), (7, 5)],
        "D": [(9, 2), (9, 3), (9, 4), (9, 5)],
    }
    COSTS = {"A": 1, "B": 10, "C": 100, "D": 1000}

    def __init__(self) -> None:
        self.complete = False
        self.best_score = 250000
        self.start_map = {
            (1, 1): None,
            (2, 1): None,
            (3, 1): None,
            (4, 1): None,
            (5, 1): None,
            (6, 1): None,
            (7, 1): None,
            (8, 1): None,
            (9, 1): None,
            (10, 1): None,
            (11, 1): None,
            (3, 2): None,
            (3, 3): None,
            (3, 4): None,
            (3, 5): None,
            (5, 2): None,
            (5, 3): None,
            (5, 4): None,
            (5, 5): None,
            (7, 2): None,
            (7, 3): None,
            (7, 4): None,
            (7, 5): None,
            (9, 2): None,
            (9, 3): None,
            (9, 4): None,
            (9, 5): None,
        }
        self.complete_map = {
            (1, 1): None,
            (2, 1): None,
            (3, 1): None,
            (4, 1): None,
            (5, 1): None,
            (6, 1): None,
            (7, 1): None,
            (8, 1): None,
            (9, 1): None,
            (10, 1): None,
            (11, 1): None,
            (3, 2): "A",
            (3, 3): "A",
            (3, 4): "A",
            (3, 5): "A",
            (5, 2): "B",
            (5, 3): "B",
            (5, 4): "B",
            (5, 5): "B",
            (7, 2): "C",
            (7, 3): "C",
            (7, 4): "C",
            (7, 5): "C",
            (9, 2): "D",
            (9, 3): "D",
            (9, 4): "D",
            (9, 5): "D",
        }

    def take_turn(self, cave_map: Dict[Tuple[int, int], str], total_cost: int) -> None:
        """Recursive function to walk through possible solutions"""
        # print(f"Current Score: {total_cost}. Best Score: {self.best_score}")
        # self.print_cave(cave_map)
        if total_cost > self.best_score:
            # print("Already over max best score, returning...")
            return None
        if total_cost + self.best_from_here(cave_map) > self.best_score:
            # print("Can't theoretically win from here. Returning...")
            return None

        possibles_moves = self.get_possible_moves(cave_map)
        if len(possibles_moves) == 0:
            if self.is_complete(cave_map) is True:
                # self.print_cave(cave_map)
                return total_cost
            # print("No More Moves Possible, len(possible_moves) = 0. Returning...")
            return None

        for move in possibles_moves:
            new_map = self.do_move(cave_map, move)
            # if total_cost == 0:
            #   print(f"First Move: {move[0]} to {move[1]}")
            #  self.print_cave(new_map)
            # else:
            #   print(f"Move: {move[0]} to {move[1]}")
            #  self.print_cave(new_map)
            move_cost = self.calculate_move_cost(cave_map, move)
            if total_cost == 0:
                start = perf_counter()
            result = self.take_turn(new_map, total_cost + move_cost)
            if total_cost == 0:
                end = perf_counter()
                print(f"Move {move} exhausted in {int(end-start)} seconds")
            if result is not None:
                if result < self.best_score:
                    print(f"New Best Score = {result}")
                self.best_score = result
        # print("No More Moves Possible, end of function, returning...")
        return None

    def get_possible_moves(self, cave_map: Dict[Tuple[int, int], str]):
        """Returns list of moves possible from this map"""
        moves = []
        viable_moves = []

        start_points = list(AmphipodCave.HALL_STOP_POINTS)
        for room_x in range(3, 10, 2):
            for y in range(2, 6):
                if cave_map[(room_x, y)] != ".":
                    start_points.append((room_x, y))
                    break

        for start_point in cave_map:
            if cave_map[start_point] is not None:
                end_points = self.get_valid_endpoints(start_point, cave_map)
                if end_points is not None:
                    for end_point in end_points:
                        moves.append((start_point, end_point))

        for move in moves:
            if self.is_viable(move, cave_map) is True:
                viable_moves.append(move)

        for move in viable_moves:
            if self.is_home_move(move, cave_map) is True:
                return [
                    move
                ]  # If there is an opportunity to move something to home space, do that

        return viable_moves

    def is_home_move(self, move, cave_map) -> bool:
        """Returns true if this move will take a piece to its final place"""
        start, end = move
        colour = cave_map[start]

        if end in AmphipodCave.ROOMS[colour]:
            return True

        return False

    def interim_locations(
        self, start: Tuple[int, int], end: Tuple[int, int]
    ) -> Set[Tuple[int, int]]:
        locations = set()
        start_x, start_y = start
        end_x, end_y = end

        if start_x < end_x:
            for x in range(start_x + 1, end_x + 1):
                locations.add((x, 1))
        else:
            for x in range(end_x, start_x):
                locations.add((x, 1))

        if start_y > 2:
            for y in range(start_y - 1, 1, -1):
                locations.add((start_x, y))

        if end_y > 1:
            for y in range(end_y, 1, -1):
                locations.add((end_x, y))

        return locations

    def is_viable(self, move, cave_map) -> bool:
        """Returns true if move is possible (i.e. no blockers)"""
        start, end = move
        interim_locations = self.interim_locations(start, end)
        interim_locations.add(end)
        interim_locations.discard(start)
        for location in interim_locations:
            if cave_map[location] is not None:
                return False
        return True

    def is_home(self, location, cave_map) -> bool:
        """Returns True if this location is home (i.e. no more moves needed)"""
        colour = cave_map[location]
        my_room = AmphipodCave.ROOMS[colour]
        if location not in my_room:
            return False
        if location == my_room[-1]:
            return True
        if location == my_room[-2]:
            if cave_map[my_room[-1]] == colour:
                return True
            return False
        if location == my_room[-3]:
            if cave_map[my_room[-2]] == colour and cave_map[my_room[-1]] == colour:
                return True
            return False
        if location == my_room[-4]:
            if (
                cave_map[my_room[-3]] == colour
                and cave_map[my_room[-2]] == colour
                and cave_map[my_room[-1]] == colour
            ):
                return True
            return False
        return False

    def get_valid_endpoints(
        self, location: Tuple[int, int], cave_map: Dict[Tuple[int, int], str]
    ) -> List[Tuple[int, int]]:
        """Returns list of end points that amphipod at location can go on the next move"""

        if self.is_home(location, cave_map):
            return []

        colour = cave_map[location]
        room = AmphipodCave.ROOMS[colour]

        end_points = []

        if location not in AmphipodCave.HALL_STOP_POINTS:
            end_points.extend(AmphipodCave.HALL_STOP_POINTS)

        for i in range(3, -1, -1):
            if cave_map[room[i]] is None:
                end_points.append(room[i])
            if cave_map[room[i]] is not colour:
                break
        return end_points

    def do_move(
        self,
        cave_map: Dict[Tuple[int, int], str],
        move: Tuple[Tuple[int, int], Tuple[int, int]],
    ) -> Dict[Tuple[int, int], str]:
        """Updates Map to reflect requested move"""
        start, end = move
        if cave_map[start] is None:
            print("Error")
        if cave_map[end] is not None:
            print("Error")

        new_map = cave_map.copy()

        new_map.update({end: new_map[start]})
        new_map.update({start: None})

        # print(f"Move {new_map[end]} from {start} to {end}")
        return new_map

    def is_complete(self, cave_map: Dict[Tuple[int, int], str]):
        """Returns True is map is in a completed state"""
        complete = True
        for location in cave_map:
            if cave_map[location] != self.complete_map[location]:
                complete = False
                break
        self.complete = complete
        return complete

    def best_from_here(self, cave_map: Dict[Tuple[int, int], str]) -> int:
        """Returns best theoretical score from this map"""
        if cave_map[(9, 5)] != "D":
            return 17000
        if cave_map[(9, 4)] != "D":
            return 10000
        if cave_map[(9, 3)] != "D":
            return 5000
        if cave_map[(9, 2)] != "D":
            return 2000
        return 0

    def calculate_move_cost(
        self,
        cave_map: Dict[Tuple[int, int], str],
        move: Tuple[Tuple[int, int], Tuple[int, int]],
    ) -> int:
        """Returns the cost of moving an Amphipod to a given location"""
        origin, destination = move
        origin_x, origin_y = origin
        dest_x, dest_y = destination

        colour = cave_map[origin]
        cost = AmphipodCave.COSTS[colour]

        total = 0

        total += abs(dest_x - origin_x)
        total += origin_y - 1
        total += dest_y - 1

        total *= cost
        return total

    def print_cave(self, cave_map):
        print("#############")
        print("#", end="")
        for i in range(1, 12):
            location = (i, 1)
            occupant = cave_map[location]
            if occupant is None:
                print(".", end="")
            else:
                print(f"{occupant}", end="")
        print("#")
        print("###", end="")
        for j in range(2, 6):
            if j > 2:
                print("  #", end="")
            for i in range(3, 11, 2):
                location = (i, j)
                occupant = cave_map[location]
                if occupant is None:
                    print(".#", end="")
                else:
                    print(f"{occupant}#", end="")
            if j == 2:
                print("##")
            else:
                print()
        print("  #########  ")
        print()
