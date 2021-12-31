def main():
    input = read_from_file("Day1\DayOneInput")
    count = how_many_increments(input)
    print("DAY 1 PART 1 RESULT")
    print("===================")
    print("Total Increments: " + str(count))
    new_data = create_sliding_window(input)
    count = how_many_increments(new_data)
    print("DAY 1 PART 2 RESULT")
    print("===================")
    print("Total Increments: " + str(count))


def how_many_increments(data: list) -> int:
    """Returns int representing number of times an entry in a list is a larger number than that before it"""
    count = 0
    for x in range(1,len(data)):
        if data[x] > data[x-1]:
            count += 1
    return count

def create_sliding_window(input: list) -> int:
    """Return new list where each entry is the sum of three entries in the previous list"""
    output =[]
    if len(input) < 3:
        return None
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