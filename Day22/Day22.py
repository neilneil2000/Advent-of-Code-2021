from Reactor import Reactor

def main():

    my_lovely_reactor = Reactor()
    my_lovely_reactor.test_overlap()

    input = read_input_file("Day22\DayTwentyTwoInput")
    values = process_input_file(input)
    answer = how_many_on_basic(values)
    print(f'Answer to Part 1. Total Lights on: {answer}')

def how_many_on_basic(values: list) -> int:
    size = 101
    big_array = [[[0 for x in range(size)] for y in range(size)] for z in range(size)]
    offset = 50
    min_boundary = -50 + offset
    max_boundary = 50 + offset + 1
    for row in values:
        x,y,z = row[1]
        x[0] += offset
        x[1] += offset
        y[0] += offset
        y[1] += offset
        z[0] += offset
        z[1] += offset

        x[0] = max(x[0],min_boundary)
        x[1] = min(x[1]+1, max_boundary)
        y[0] = max(y[0],min_boundary)   
        y[1] = min(y[1]+1, max_boundary)
        z[0] = max(z[0],min_boundary)
        z[1] = min(z[1]+1, max_boundary)
        
        if x[0] <= x[1] and y[0] <= y[1] and z[0] <= z[1]:
            for k in range(z[0], z[1]):
                for j in range(y[0], y[1]):
                    for i in range(x[0], x[1]):
                        if row[0] == 'on':
                            big_array[k][j][i] = 1
                        else:
                            big_array[k][j][i] = 0
    count_on  = 0
    for k in range(size):
            for j in range(size):
                for i in range(size):
                    if big_array[k][j][i] == 1:
                        count_on += 1

    return count_on



def process_input_file(input: list) -> list:
    output = []
    for line in input:
        on_off,co_ords = line.split(' ')
        co_ords = co_ords.split(',')
        x,y,z = co_ords
        x = x.split('=')[1].split('..')
        x[0] = int(x[0])
        x[1] = int(x[1])
        y = y.split('=')[1].split('..')
        y[0] = int(y[0])
        y[1] = int(y[1])
        z = z.split('=')[1].split('..')
        z[0] = int(z[0])
        z[1] = int(z[1])
        cuboid = (on_off, (x,y,z))
        output.append(cuboid)
    return output


def read_input_file(filename) -> list:
    input = []
    with open(filename, 'r') as f:
        for line in f:
            input.append(line.strip())
    return input




if __name__ == '__main__':
    main()