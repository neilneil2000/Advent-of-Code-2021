from OctopusGrid import Grid

def main():
    octopi = Grid("Day11/DayElevenInput")
    octopi.compute_steps(100)
    print(f'{octopi.total_flashes} flashes in total')

    octopi.compute_steps_until_sync()

if __name__ == "__main__":
    main()