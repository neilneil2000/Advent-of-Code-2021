def main():
    input = read_input_file("Day8/DayEightTestInput")
    print(input)

def read_input_file(filename):
    file_info = []
    with open(filename,'r') as f: #Using 'with; implicitly handles exceptions and f.close()
        while True:
            line = f.readline()
            if not line:
                break
            file_info.append(line.strip())
    return file_info




if __name__ == '__main__':
    main()