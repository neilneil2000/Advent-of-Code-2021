from functools import lru_cache
import statistics
import sys

def main():
    crab_locations = read_input_file("Day7/DaySevenInput")

    med = statistics.median(crab_locations) #Fast way for basic method
    print(int(med))
    pos, fuel = brute_force_exponential(crab_locations)
    print(pos)
    print(fuel)


def brute_force_exponential(start_positions):
    highest = max(start_positions)
    sys.setrecursionlimit(2*highest+16) #Could replace "highest" with calculating the biggest step between crab start_positions but this does the job
    lowest = min(start_positions)
    working_total = 0
    winning_total = 9999999999999999 #arbitrarily high
    winning_position = 0
    for end_position in range(lowest,highest):
        for crab in start_positions:
            working_total += triangle(abs(crab-end_position))
        if working_total < winning_total:
            winning_total = working_total
            winning_position = end_position
        working_total = 0
    return winning_position, winning_total

@lru_cache(maxsize=None)
def triangle(x):
    """
    Returns triangular number x 
    """
    if x == 0:
        return 0
    if x > 1:
        t = triangle(x-1)
        return t + x
    return 1


def brute_force(start_positions):
    highest = max(start_positions)
    lowest = min(start_positions)
    working_total = 0
    winning_total = 9999999999999999 #arbitrarily high
    winning_position = 0
    for x in range(lowest,highest):
        for item in start_positions:
            working_total += abs(x-item)
        if working_total < winning_total:
            winning_total = working_total
            winning_position = x
        working_total = 0
    return winning_position, winning_total

def read_input_file(filename):
    f = open(filename,'r')
    file = []
    while True:
        line = f.readline()
        if not line:
            break
        line = line.split(',')
        file.extend(line)
    f.close()
    for x in range(0,len(file)):
        file[x] = int(file[x])
    return file

if __name__ == '__main__':
    main()