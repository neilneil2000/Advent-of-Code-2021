from SensorManager import SensorManager


def main():
    input = read_input_file("Day19\DayNineteenInput")
    my_Sensors = SensorManager()
    my_Sensors.process_sensor_report(input) 
    my_Sensors.align_all_sensors()
    my_Sensors.confirm_beacons()
    print(f'{len(my_Sensors.beacons)} Beacons found')

    manhattan_distance = my_Sensors.get_biggest_distance()
    print(f'Biggest Distance Between Sensors is {manhattan_distance}')
    print(f'END')


   


def read_input_file(filename: str) -> list:
    input = []
    with open(filename, 'r') as f:
        for line in f:
            input.append(line.strip())
    return input

if __name__ == '__main__':
    main()