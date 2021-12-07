import statistics

def main():
    crab_locations = read_input_file("Day7/DaySevenInput")
    print(crab_locations)
    med = statistics.median(crab_locations)
    print(med)
    pos, fuel = brute_force_exponential(crab_locations)
    print(pos)
    print(fuel)


def brute_force_exponential(start_positions):
    highest = max(start_positions)
    lowest = min(start_positions)
    working_total = 0
    winning_total = 9999999999999999 #arbitrarily high
    winning_position = 0
    for x in range(lowest,highest):
        for item in start_positions:
            for y in range(1,abs(x-item)+1):
                working_total += y
        if working_total < winning_total:
            winning_total = working_total
            winning_position = x
        working_total = 0
    return winning_position, winning_total

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