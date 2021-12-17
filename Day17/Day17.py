def main():
    x_bounds = (236,262)
    y_bounds = (-78,-58)
    y_max = 0
    valid_counter = 0
    min_x_velocity = 0 #First triangular number >= x_lowest
    x = 0
    while x < x_bounds[0]:
        min_x_velocity += 1
        x = triangular(min_x_velocity)
    max_x_velocity = x_bounds[1]
    min_y_velocity = y_bounds[0]
    max_y_velocity = (y_bounds[0] + 1) * -1

    for y_velocity in range(min_y_velocity,max_y_velocity + 1):
        for x_velocity in range(min_x_velocity,max_x_velocity + 1):
         shot_y_max = shot_emulator(x_bounds, y_bounds, x_velocity, y_velocity)
         if shot_y_max is not None:
             y_max = max(y_max, shot_y_max)
             valid_counter += 1
    print(f'y_max is {y_max}')
    print(f'Number of options is {valid_counter}')

def triangular(n):
    """ Return nth triangular number"""
    return int(0.5 * (n * (n+1)))

def shot_emulator(x_bounds, y_bounds, x_velocity, y_velocity):
    x_lower, x_upper = x_bounds
    y_lower, y_upper = y_bounds
    x_position = 0
    y_position = 0
    step_counter = 0
    y_max = 0
    while True:
        x_position += x_velocity
        if x_velocity > 0:
            x_velocity -= 1
        y_position += y_velocity
        y_velocity -= 1
        y_max = max(y_max, y_position)
        if x_position > x_upper:
            return None
        if y_position < y_lower:
            return None
        if x_position >= x_lower and y_position <= y_upper:
            return y_max
        step_counter += 1

if __name__ == "__main__":
    main()