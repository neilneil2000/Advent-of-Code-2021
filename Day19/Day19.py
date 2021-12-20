from SensorManager import SensorManager


def main():
    input = read_input_file("Day19\DayNineteenInput")
    my_Sensors = SensorManager()
    my_Sensors.process_sensor_report(input)
    
    my_Sensors.align_all_sensors()
    #for sensor in range(0,39):
     #   my_Sensors.align_sensors(3,sensor)
      #  my_Sensors.align_sensors(4,sensor)
       # my_Sensors.align_sensors(22,sensor)
       # my_Sensors.align_sensors(25,sensor)
       # my_Sensors.align_sensors(27,sensor)
       # my_Sensors.align_sensors(31,sensor)
       # my_Sensors.align_sensors(32,sensor)
       # my_Sensors.align_sensors(34,sensor)

    my_Sensors.confirm_beacons()
    print(f'{len(my_Sensors.beacons)} Beacons found')
    print(f'END')


   


def read_input_file(filename: str) -> list:
    input = []
    with open(filename, 'r') as f:
        for line in f:
            input.append(line.strip())
    return input

if __name__ == '__main__':
    main()