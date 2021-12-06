def main():
    input_file = "Day6/DaySixInput"
    current_day = 0
    lantern_fish = read_input_file(input_file)
    day_target = 80
    incremental_days = day_target - current_day
    fish_summary = summarise_fish(lantern_fish)
    age_by_days_fast(fish_summary,incremental_days)
    current_day += incremental_days
    total_fish = calculate_total_fish(fish_summary)

    print("DAY 6 PART 1 COMPLETE:")
    print("======================")
    print("Number of fish after " + str(current_day) + " days: " + str(total_fish))
    
    #lantern_fish = read_input_file(input_file)
    day_target = 256
    incremental_days = day_target - current_day
    age_by_days_fast(fish_summary,incremental_days)
    total_fish = calculate_total_fish(fish_summary)

    print("DAY 6 PART 2 COMPLETE:")
    print("======================")
    print("Number of fish after " + str(current_day) + " days: " + str(total_fish))

def calculate_total_fish(fish_list):
    total_fish = 0
    for fish in fish_list:
        total_fish += fish
    return total_fish

def age_by_days_fast(fish,days):
    for x in range(0,days):
        fish.append(fish.pop(0))
        fish[6] += fish[8]

def age_by_days(lantern_fish, days):
    
    for x in range(0,days):
        how_many_fish = len(lantern_fish)
        for y in range(0,how_many_fish):
            lantern_fish[y] -= 1
        how_many_fish = len(lantern_fish)
        for y in range(0,how_many_fish):
            if lantern_fish[y] < 0:
                lantern_fish[y] = 6
                lantern_fish.append(8)

def summarise_fish(fish):
    summary =[0,0,0,0,0,0,0,0,0]
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