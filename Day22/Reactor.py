from enum import Enum

class new_vs_current(Enum):
    #too_low = 0
    #overlap_low = 1
    fits_within = 2
    #overlap_high = 3
    #too_high = 4
    overlap_both = 5
    no_overlap = 6
    intersect = 7
    
class Reactor:

    def __init__(self):
        self.on_areas = []
        self.off_areas = 
         []

    def process_pair(self, current_cuboid, new_cuboid):
        overlap = self.check_3d_overlap(current_cuboid, new_cuboid)
        if overlap == new_vs_current.intersect:
            self.process_intersection()
        elif overlap == new_vs_current.overlap_both:
            self.active_areas.append(new_cuboid)
            self.active_areas.remove(current_cuboid)
        elif overlap == new_vs_current.no_overlap:
            self.active_areas.append(new_cuboid)
    
    def condense_overlap(self, overlaps: list):
        if overlaps.count(new_vs_current.fits_within) == 3:
            return new_vs_current.fits_within       
        if overlaps.count(new_vs_current.overlap_both) == 3:
            return new_vs_current.overlap_both      
        if overlaps.count(new_vs_current.no_overlap) > 0:
            return new_vs_current.no_overlap
        return new_vs_current.intersect

    def check_3d_overlap(self, current_cuboid: list, new_cuboid: list) -> list:
        overlaps = [None, None, None]
        for i in range(3):
            overlaps[i] = self.check_overlap(current_cuboid[i],new_cuboid[i])
        overlap_verdict = self.condense_overlap(overlaps)

    def process_intersection(self, current_cuboid, new_cuboid):
        pass

                   

    def check_overlap(self, current_region: list, new_region: list) -> new_vs_current:
        """Checks overlap on 1 axis (The +1/-1 are used as regions are INCLUSIVE both ends)"""
        current_lower, current_upper = current_region
        new_lower, new_upper = new_region

        if new_upper < current_lower - 1:
            return new_vs_current.no_overlap
            #return new_vs_current.too_low # Top of New is lower than Bottom of current
        elif new_lower > current_upper + 1:
            return new_vs_current.no_overlap
            #return new_vs_current.too_high # Bottom of new is higher than Bottom of current
        elif new_lower >= current_lower and new_upper <= current_upper:
            return new_vs_current.fits_within
        elif new_lower >= current_lower:
            return new_vs_current.intersect
            #return new_vs_current.overlap_high
        elif new_upper <= current_upper:
            return new_vs_current.intersect
            #return new_vs_current.overlap_low
        return new_vs_current.overlap_both

    def switch_on_in_region(self):
        pass

    def switch_off_in_region(self):
        pass

def test_overlap(self):
        main_region = [-10,20]
        test_region = {
            'wide_region' : [-60,100],
            'lower_region' : [-20,-15],
            'low_mid_region' : [-50, -11],
            'low_mid_region2' : [-40,5],
            'mid_region' : [-3,16],
            'upper_mid_region' : [15,60],
            'upper_mid_region2' : [21,70],
            'upper_region' : [80,100]
            }
        for new_region in test_region.values():
            print(f'Testing {new_region} against existing {main_region}')
            answer = self.check_overlap(main_region, new_region)
            print(f'Response: {answer}')
            print()