from typing import Counter


def main():
    input = read_from_file("DayOneInput")
    count = how_many_increments(input)
    print("DAY 1 PART 1 RESULT")
    print("===================")
    print("Total Increments: " + str(count))
    new_data = create_sliding_window(input)
    count = how_many_increments(new_data)
    print("DAY 1 PART 2 RESULT")
    print("===================")
    print("Total Increments: " + str(count))


def how_many_increments(data):
    count = 0
    for x in range(1,len(data)):
        if data[x] > data[x-1]:
            count += 1
    return count

def create_sliding_window(input):
    output =[]
    for x in range(2,len(input)):
        output.append(input[x]+input[x-1]+input[x-2])
    return output

def read_from_file(filename):
    f = open(filename, 'r')
    line_number = 0
    data =[]
    while True:
        line_number += 1
        line = f.readline()
        if not line:
            break    
        value = int(line.strip())
        data.append(value)
    f.close()
    return data


if __name__ == '__main__':
    main()