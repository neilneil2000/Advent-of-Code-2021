from typing import Tuple


class Amphipod:
    """Representation of an individual Amphipod"""

    COSTS = {"A": 1, "B": 10, "C": 100, "D": 1000}

    def __init__(self, colour: str, location: Tuple[int, int]):
        self.colour = colour
        self.cost = Amphipod.COSTS[colour]
        self.positions = [location]
        self.done = False

    def move(self, location: Tuple[int, int]) -> None:
        """Move Amphipod to new location"""
        self.positions.append(location)
