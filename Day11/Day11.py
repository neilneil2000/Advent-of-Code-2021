from OctopusGrid import Grid

def main():
    octopi = Grid("Day11/DayElevenInput")
    octopi.compute_steps(300)
    print(f'{octopi.total_flashes} flashes in total')

if __name__ == "__main__":
    main()