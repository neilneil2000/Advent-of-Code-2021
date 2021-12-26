from CucumberGrid import Grid

def main():
    input = read_input_file("Day25\DayTwentyFiveInput")
    ocean_floor = Grid(input)
    print(f'START POSITION')
    print(f'==============')
    ocean_floor.print_floor()
    rounds = ocean_floor.move_until_static()
    print(f'POSITION AFTER ROUND {rounds}')
    print(f'==============')
    ocean_floor.print_floor()
    print('END')

def read_input_file(filename):
    output = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            line = list(line)
            output.append(line)
    return output


if __name__ == '__main__':
    main()