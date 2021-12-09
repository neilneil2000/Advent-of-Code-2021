from map import Map

def main():
    cave = Map("Day9/DayNineInput")
    cave.find_low_points()
    print(f'Found {len(cave.low_points)} Low Points')
    risk = cave.calculate_risk()
    print(f'Risk Level is {risk}')


if __name__ == '__main__':
    main()