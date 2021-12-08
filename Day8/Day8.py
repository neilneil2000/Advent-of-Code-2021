from Display import SevenSegment

def main():
    input = read_input_file("Day8/DayEightInput")

    count = 0
    for entry in input:
        for value in entry['code']:
            length = len(value)
            if length == 2:
                count += 1
            elif length == 3:
                count += 1
            elif length == 4:
                count += 1
            elif length == 7:
                count += 1

    print("DAY 8 PART 1 Complete")
    print("=====================")
    print(count)

    solution = 0
    for row in input:
        solution += solve_row(row)
    print("DAY 8 PART 2 Complete")
    print("=====================")
    print(solution)

def solve_row(row):
    segment = SevenSegment()
    sixer_clues = set()
    for clue in row['hints']:
        segment.process_clue(clue)
        if len(clue) == 6:
            sixer_clues.add(clue)
    if not segment.is_solved():
        for clue in row['code']:
            segment.process_clue(clue)

    segment.check_six_lengths(sixer_clues)
    answer = segment.decode(row['code'])

    return answer        
    

def read_input_file(filename):
    file_info = []
    with open(filename,'r') as f: #Using 'with; implicitly handles exceptions and f.close()
        while True:
            line = f.readline()
            new_line = []
            if not line:
                break
            line = line.strip().split('|')
            for item in line:
                new_line.append(item.split())
            file_info.append({'hints':new_line[0],'code':new_line[1]})
    return file_info




if __name__ == '__main__':
    main()