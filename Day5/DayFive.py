from types import coroutine


def main():
    input = read_input_file("DayFiveInput")
    p1_input = remove_diagonals(input)
    danger_zones = {}
    danger_zones = calculate_danger_zones(danger_zones,p1_input)
    danger_points = count_danger_zones(danger_zones)
    print("DAY 5 PART 1 COMPLETE:")
    print("======================")
    print("Danger Points: " + str(danger_points))
    p2_input = list(input)
    danger_zones = {}
    danger_zones = calculate_danger_zones(danger_zones,p2_input)
    danger_points = count_danger_zones(danger_zones)
    print("DAY 5 PART 2 COMPLETE:")
    print("======================")
    print("Danger Points: " + str(danger_points))


def remove_diagonals(input):
    output = list(input)
    x = 0
    while x < len(output): 
        a = output[x][0]
        b = output[x][1]
        if a[0] != b[0] and a[1] != b[1]:
            del output[x]
        else:
            x += 1
    return output

def read_input_file(filename):
    lines = []
    f = open(filename,'r')
    while True:
        l = f.readline().strip()
        if not l:
            break
        l = l.split(' -> ')
        l[0] = l[0].split(',')
        l[1] = l[1].split(',')

        l[0][0] = int(l[0][0])
        l[0][1] = int(l[0][1])
        l[1][0] = int(l[1][0])
        l[1][1] = int(l[1][1])
        
        l[0] = tuple(l[0])
        l[1] = tuple(l[1])

        lines.append(l)
    return lines


def calculate_danger_zones(danger_zones,line_points):
    for x in range(0,len(line_points)):
        line = expand_line(line_points[x])
        update_danger_list(danger_zones,line)
    return danger_zones

def expand_line(points):
    """
    Take start and finish point and return all points in line
    """
    start = points[0]
    end = points[1]
    full_line = list(points)
    if start[0] == end[0]:
        if start[1] > end[1]:
            lower = end[1]
            upper = start[1]
        else:
            lower = start[1]
            upper = end[1]
        for x in range(lower,upper):
            full_line.append((start[0],x))
    elif start[1] == end[1]:
        if start[0] > end[0]:
            lower = end[0]
            upper = start[0]
        else:
            lower = start[0]
            upper = end[0]
        for x in range(lower,upper):
            full_line.append((x,start[1]))
    else: #Handle Diagnoals
        if start[0] < end[0] and start[1] < end[1]:
            diff = end[0]-start[0]
            for x in range(0,diff):
                full_line.append((start[0]+x,start[1]+x))
        elif start[0] > end[0] and start[1] > end[1]:
            diff = start[0]-end[0]
            for x in range(0,diff):
                full_line.append((start[0]-x,start[1]-x))
        elif start[0] < end[0] and start[1] > end[1]:
            diff = end[0]-start[0]
            for x in range(0,diff):
                full_line.append((start[0]+x,start[1]-x))
        else:
            diff = start[0]-end[0]
            for x in range(0,diff):
                full_line.append((start[0]-x,start[1]+x))

    #Remove duplicates from full_line
    final_line = []
    for point in full_line:
        if point not in final_line:
            final_line.append(point)
    return final_line

def update_danger_list(danger_zones,line):
    for point in line:
        if point in danger_zones.keys():
            danger_zones.update({point:danger_zones[point]+1})
        else:
            danger_zones.update({point:1})
    
def count_danger_zones(zones,threshold=2):
    counter = 0
    for danger_level in zones.values():
        if danger_level >= threshold:
            counter += 1
    return counter

if __name__ == '__main__':
    main()