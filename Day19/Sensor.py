class Sensor:

    MAX_RANGE = 500

    def __init__(self, id):
        self.sensor_id = id
        self.orientation = (0,0,0) # (x,y,z) orientation relative to Sensor 0
        self.offset = (0,0,0) #(x,y,z) offset relative to Sensor 0
        if id == 0:
            self.location_confirmed = True
        else:
            self.location_confirmed = False
        self.beacons = []
        self.original_beacons = []

    def set_offset(self, offset: tuple) -> None:
        self.offset = offset
        for i, beacon in enumerate(self.beacons):
            self.beacons[i] = self.tuple_add(beacon, offset)

    def rotate(self, rotation: tuple) -> None:
        self.orientation = rotation
        for i, beacon in enumerate(self.beacons):
            self.beacons[i] = self.apply_rotation(beacon, rotation)

    def apply_rotation(self, location: tuple, rotation: tuple) -> tuple:
        """Rotate in 3 dimensions"""
        x, y, z = location
        #Work out rotation steps about each axis
        xr, yr, zr = rotation
        xr = int(xr / 90)
        yr = int(yr / 90)
        zr = int(zr / 90)

        #Rotate about x Axis
        for _ in range(0, xr):
            y ^= z
            z ^= y
            y ^= z
            z *= -1
            
        #Rotate about y Axis
        for _ in range(0, yr):
            x ^= z
            z ^= x
            x ^= z
            x *= -1

        #Rotate about z Axis
        for _ in range(0, zr):
            x ^= y
            y ^= x
            x ^= y
            y *= -1
                    
        return (x, y, z)

    def get_offset_beacons(self, offset: tuple) -> list:
        offset_beacons = []
        for beacon in self.beacons:
            offset_beacon = self.tuple_add(beacon, offset)
            offset_beacons.append(offset_beacon)
        return offset_beacons

    def tuple_add(self, a: tuple, b:tuple) -> tuple:
        """Subtracts each element in tuple b from tuple a"""
        return (a[0] + b[0], a[1] + b[1], a[2] + b[2])

    def add_beacon(self, location: tuple):
        self.beacons.append(location)
        self.original_beacons.append(location)