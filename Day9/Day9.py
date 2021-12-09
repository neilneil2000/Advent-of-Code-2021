from map import Map

def main():
    cave = Map("Day9/DayNineInput")
    cave.find_low_points()
    risk = cave.calculate_risk()
    print(f'DAY 9 PART 1 COMPLETE:')
    print(f'======================')
    print(f'Risk Level is {risk}')
    print()
    cave.mark_basins()
    cave.calculate_basin_sizes()
    cave.sort_basin_sizes()
    answer = cave.basin_sizes.pop() * cave.basin_sizes.pop() * cave.basin_sizes.pop()
    print(f'DAY 9 PART 2 COMPLETE:')
    print(f'======================')
    print(f'Product of LARGEST 3 basins is: {answer}')
    print()



if __name__ == '__main__':
    main()
