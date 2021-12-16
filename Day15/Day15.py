from cave import Cave

def main():
    my_cave = Cave("Day15\DayFifteenTestInput")

    lowest_path = my_cave.get_best((0,0),99999999999,(0,0))
    print(f'Lowest Path Found has cost: {lowest_path}')
    print('END')




if __name__ == '__main__':
    main()