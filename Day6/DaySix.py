def main():
    input_file = "Day6/DaySixInput"
    lantern_fish = read_input_file(input_file)
    fish_summary = summarise_fish(lantern_fish)

    current_day = 0

    #Part 1
    day_target = 80
    incremental_days = day_target - current_day
    age_by_days(fish_summary,incremental_days)
    current_day += incremental_days
    print_result(1,current_day,fish_summary)
    
    #Part 2
    day_target = 256
    incremental_days = day_target - current_day
    age_by_days(fish_summary,incremental_days)
    current_day += incremental_days
    print_result(2,current_day,fish_summary)

def print_result(part,day,fish):
    total_fish = calculate_total_fish(fish)
    print("DAY 6 PART " + str(part) +" COMPLETE:")
    print("======================")
    print("Number of fish after " + str(day) + " days: " + str(total_fish))

def calculate_total_fish(fish_list):
    total_fish = 0
    for fish in fish_list:
        total_fish += fish
    return total_fish

def age_by_days(fish,days):
    """
    Calculate how many fish with x days to reproduce
    Each day every number decrements and at 0 a new fish is born
    New fish will reproduce after 8 days
    Existing fish will reproduce after 6 days
    """
    for x in range(0,days):
        fish.append(fish.pop(0))
        fish[6] += fish[8]

def summarise_fish(fish):
    """
    Group fish into number of days left to reproduce
    Store total in array where index = days to go
    """
    summary = [0,0,0,0,0,0,0,0,0]
    for item in fish:
        summary[item] += 1
    return summary

def read_input_file(filename):
    f = open(filename,'r')
    r = f.readline().split(',')
    for x in range(0,len(r)):
        r[x] = int(r[x])
    f.close()
    return r

if __name__ == '__main__':
    main()