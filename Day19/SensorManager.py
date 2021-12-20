from Sensor import Sensor

class SensorManager:

    SENSOR_ID_LEFT_OFFSET = 12
    SENSOR_ID_RIGHT_OFFSET = 4

    def __init__(self):
        self.sensors = {}
        self.beacons = set()

    def get_biggest_distance(self) -> int:
        max_distance = 0
        for sensor_a_id in range(0,len(self.sensors)):
            for sensor_b_id in range(sensor_a_id+1,len(self.sensors)):
                new_distance = self.calc_distance_between_sensors(sensor_a_id, sensor_b_id)
                max_distance = max(max_distance, new_distance)
        return max_distance
    
    def calc_distance_between_sensors(self, a_id, b_id):
        a_location = self.sensors[a_id].offset
        b_location = self.sensors[b_id].offset
        difference = self.tuple_subtract(a_location, b_location)
        x, y, z = difference
        if x < 0:
            x *= -1
        if y < 0:
            y *= -1
        if z < 0:
            z *= -1
        return x + y + z



    def align_all_sensors(self):
        confirmed_sensors = set()
        checked_pairs = set()
        while len(confirmed_sensors) < len(self.sensors):
            for id,sensor in self.sensors.items():
                if sensor.location_confirmed == True:
                    confirmed_sensors.add(id)
            for sensor_id in self.sensors.keys():
                for confirmed_id in confirmed_sensors:
                    if self.sensors[sensor_id].location_confirmed == False:
                        if (confirmed_id, sensor_id) not in checked_pairs:
                            self.align_sensors(confirmed_id, sensor_id)
                            checked_pairs.add((confirmed_id, sensor_id))



    def confirm_beacons(self):
        for sensor in self.sensors.values():
            for beacon in sensor.beacons:
                self.beacons.add(beacon)

    def align_sensors(self, sensor_a_id, sensor_b_id):
        #for each rotation check whether there's alignment (this can be optimised to just unique rotations
        for step in range(0,24):
            offset_count = self.offset_between_sensors(sensor_a_id,sensor_b_id)
            if max(offset_count.values()) >= 12:
                for location,count in offset_count.items():
                    if count>=12:
                        print(f'Sensor: {sensor_b_id} confirmed at {location}: {count} ) - Validator: {sensor_a_id}')
                        self.sensors[sensor_b_id].set_offset(location)
                        self.sensors[sensor_b_id].location_confirmed = True
                        return True
            self.sensors[sensor_b_id].rotate_to_next()
        return False

    def tuple_subtract(self, a: tuple, b:tuple) -> tuple:
        """Subtracts each element in tuple b from tuple a"""
        return (a[0] - b[0], a[1] - b[1], a[2] - b[2])

    def check_alignment(self, sensor_a_id, sensor_b_id, offset):
        """Check whether beacon patterns align if sensor_b is offset compared to sensor_a"""
        a = set(self.sensors[sensor_a_id].beacons)
        b = set(self.sensors[sensor_b_id].get_offset_beacons(offset))

        match_counter = 0

        for a_beacon in a:
            for b_beacon in b:
                if a_beacon == b_beacon:
                    match_counter += 1

        return match_counter

    def offset_between_sensors(self, confirmed_sensor_id: int, sensor_to_check_id:  int) -> dict:
        """Calculate the offsets between beacons in sensor_X to main sensor (0) """
        offsets = []
        a_beacons = self.sensors[confirmed_sensor_id].beacons
        b_beacons = self.sensors[sensor_to_check_id].beacons

        for a in a_beacons:
            for b in b_beacons:
                offset = self.tuple_subtract(a, b)
                offsets.append(offset)

        unique_offsets = set(offsets)
        offset_count = {}
        for item in unique_offsets:
            count = offsets.count(item)
            offset_count.update({item:count})

        return offset_count


    def offset_to_main_sensor(self, sensor_id:  int) -> dict:
        """Calculate the offsets between beacons in sensor_X to main sensor (0) """
        offsets = []
        a_beacons = self.sensors[0].beacons
        b_beacons = self.sensors[sensor_id].beacons

        for a in a_beacons:
            for b in b_beacons:
                offset = self.tuple_subtract(a, b)
                offsets.append(offset)

        unique_offsets = set(offsets)
        offset_count = {}
        for item in unique_offsets:
            count = offsets.count(item)
            offset_count.update({item:count})

        return offset_count
   
    def process_sensor_report(self,report: list):
        """Take input file and build Sensors"""
        current_sensor = None
        for line in report:
            if line == '':
                pass
            elif line[1] == '-':
                current_sensor = self.create_new_sensor(line)
            else:
                beacon_location = line.split(',')
                for i in range(0,len(beacon_location)):
                    beacon_location[i] = int(beacon_location[i])
                beacon_location = tuple(beacon_location)
                self.add_beacon(beacon_location,current_sensor)

    def add_beacon(self, location: list, sensor_id: int):
        sensor = self.sensors[sensor_id]
        sensor.add_beacon(location)

    def create_new_sensor(self,sensor_info: str) -> int:
        """Instantiate a new sensor with ID"""
        left = SensorManager.SENSOR_ID_LEFT_OFFSET
        right = SensorManager.SENSOR_ID_RIGHT_OFFSET
        
        sensor_id = int(sensor_info[left:-right])

        if sensor_id in self.sensors:
            print(f'ERROR: Sensor {sensor_id} already exists')
        self.sensors.update({sensor_id:Sensor(sensor_id)})

        return sensor_id
        


