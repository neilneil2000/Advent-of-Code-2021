from Caves import Caves

def main():
    caves = Caves("Day12\DayTwelveInput")
    caves.compute_paths()
    caves.print_paths()
    print('END')

if __name__ == '__main__':
    main()