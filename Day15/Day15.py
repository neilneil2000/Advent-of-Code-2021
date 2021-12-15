from cave import Cave

def main():
    my_cave = Cave("Day15\DayFifteenInput")
    my_cave.compute_path()
    print(f'Lowest Path Found has cost: {my_cave.lowest_path}')
    print('END')




if __name__ == '__main__':
    main()