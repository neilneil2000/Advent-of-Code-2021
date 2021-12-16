from cave import Cave
from time import time

def main():
    print(f'{time()}: Program Started')
    my_cave = Cave("Day15\DayFifteenInput")
    lowest_path = my_cave.get_best((0,0),99999999999,(0,0))
    print(f'Lowest Path Found has cost: {lowest_path}')
    print(f'{time()}: END')






if __name__ == '__main__':
    main()

