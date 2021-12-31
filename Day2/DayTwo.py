import csv

def main():
    input = read_from_file("Day2\DayTwoInput")
    horizontal, depth = calculate_position(input)
    print("DAY 2 PART 1 RESULT")
    print("===================")
    print("Horizontal: " + str(horizontal) + " Depth: " + str(depth))
    print("Result: " + str(horizontal*depth))

    horizontal, depth = calculate_position_two(input)
    print("DAY 2 PART 2 RESULT")
    print("===================")
    print("Horizontal: " + str(horizontal) + " Depth: " + str(depth))
    print("Result: " + str(horizontal*depth))

def calculate_position(directions: list) -> int:
    """Using Part 1 Instructions convert list of ["instruction",amount] \
        to calculate final horizontal and depth positions"""
    horizontal = 0
    depth = 0
    for x in directions:
        if x[0] == 'forward':
            horizontal += int(x[1])
        elif x[0] == 'up':
            depth -= int(x[1])
        elif x[0] == 'down':
            depth += int(x[1])
    return horizontal, depth

def calculate_position_two(directions: list) -> int:
    """Using Part 2 Instructions convert list of ["instruction",amount] \
        to calculate final horizontal and depth positions
        Note: this uses aim as an interim value and does not return it"""
    horizontal = 0
    depth = 0
    aim = 0
    for x in directions:
        if x[0] == 'forward':
            horizontal += int(x[1])
            depth += aim*int(x[1])
        elif x[0] == 'up':
            aim -= int(x[1])
        elif x[0] == 'down':
            aim += int(x[1])
    return horizontal, depth


def read_from_file(filename):
    data =[]
    with open(filename, 'r') as f:
        reader=csv.reader(f , delimiter=' ')
        for item in reader:
            data.append(item)
    return data


if __name__ == '__main__':
    main()