from SensorManager import SensorManager


def main():
    input = read_input_file("Day19\DayNineteenTestInput")
    my_Sensors = SensorManager()
    my_Sensors.process_sensor_report(input)
    my_Sensors.align_sensors(0,1)
    my_Sensors.align_sensors(0,2)
    my_Sensors.align_sensors(1,2)
    my_Sensors.align_sensors(0,3)
    my_Sensors.align_sensors(1,3)
    my_Sensors.align_sensors(3,2)
    my_Sensors.align_sensors(0,4)
    my_Sensors.align_sensors(1,4)
    my_Sensors.align_sensors(3,4)
    my_Sensors.align_sensors(4,2)

    my_Sensors.confirm_beacons()
    print(f'{len(my_Sensors.beacons)} Beacons found')



    print(my_Sensors.sensors[0].beacons)
    print()
    print(my_Sensors.sensors[1].beacons)



    my_Sensors.offset_to_main_sensor(1)
    counter = my_Sensors.check_alignment(0,1,(68,-1246,-43))
    print(counter)
    print('END')


def read_input_file(filename: str) -> list:
    input = []
    with open(filename, 'r') as f:
        for line in f:
            input.append(line.strip())
    return input

if __name__ == '__main__':
    main()