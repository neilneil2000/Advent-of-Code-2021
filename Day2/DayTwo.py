"""Solution to Day 2 of Advent of Code 2021"""
import csv
from typing import Tuple, List


def main():
    """Calculate Solutions for Part 1 and 2 and Print Results to Screen"""
    directions = read_from_file("Day2\\DayTwoInput")
    horizontal, depth = calculate_position(directions)
    print("DAY 2 PART 1 RESULT")
    print("===================")
    print("Horizontal: " + str(horizontal) + " Depth: " + str(depth))
    print("Result: " + str(horizontal * depth))

    horizontal, depth = calculate_position_two(directions)
    print("DAY 2 PART 2 RESULT")
    print("===================")
    print("Horizontal: " + str(horizontal) + " Depth: " + str(depth))
    print("Result: " + str(horizontal * depth))


def calculate_position(directions: List[Tuple[str, int]]) -> Tuple[int, int]:
    """Using Part 1 Instructions convert list of ["instruction",amount] \
        to calculate final horizontal and depth positions"""
    horizontal = 0
    depth = 0
    for step in directions:
        if step[0] == "forward":
            horizontal += int(step[1])
        elif step[0] == "up":
            depth -= int(step[1])
        elif step[0] == "down":
            depth += int(step[1])
    return horizontal, depth


def calculate_position_two(directions: List[Tuple[str, int]]) -> Tuple[int, int]:
    """Using Part 2 Instructions convert list of ["instruction",amount] \
        to calculate final horizontal and depth positions
        Note: this uses aim as an interim value and does not return it"""
    horizontal = 0
    depth = 0
    aim = 0
    for step in directions:
        if step[0] == "forward":
            horizontal += int(step[1])
            depth += aim * int(step[1])
        elif step[0] == "up":
            aim -= int(step[1])
        elif step[0] == "down":
            aim += int(step[1])
    return horizontal, depth


def read_from_file(filename: str) -> List[Tuple[str, int]]:
    """Read instruction file and return list of directions"""
    data = []
    with open(filename, "r", encoding="UTF-8") as file:
        reader = csv.reader(file, delimiter=" ")
        for item in reader:
            data.append(item)
    return data


if __name__ == "__main__":
    main()
