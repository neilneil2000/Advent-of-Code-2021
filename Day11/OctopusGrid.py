class Grid:
    
    def __init__(self,filename):
        self.energy_levels = []
        self.read_input_file(filename)
        self.total_flashes = 0
        self.flashed = set() #Positions that have flashed this round
        self.synchro_flag = False

    def process_flash(self,position):
        """Process flash of octopus at *position* """
        impacted = self.calc_flash_impact(position)
        self.increment(impacted)
        self.flashed.add(position)

    def calc_flash_impact(self,position):
        """Return list of locations that would be impacted by a flash as *position* """
        x,y = position
        impacted = set()
        impacted.add((x - 1, y - 1))    #Top Left
        impacted.add((x - 1, y))        #Top Middle
        impacted.add((x - 1, y + 1))    #Top Right
        impacted.add((x, y + 1))        #Middle Right
        impacted.add((x + 1, y + 1))    #Bottom Right
        impacted.add((x + 1, y))        #Bottom Middle
        impacted.add((x + 1, y - 1))    #Bottom Left
        impacted.add((x, y - 1))        #Middle Left
        real_impacted = impacted.copy()
        for point in impacted:
            x,y = point
            if x < 0 or y <0:
                real_impacted.remove(point)
            elif x >= len(self.energy_levels) or y >= len(self.energy_levels[0]):
                real_impacted.remove(point)
        return real_impacted

    def increment(self,positions):
        """Increment energy levels at all *positions* or everywhere if *positions* is None"""
        if positions is None:
            #increment all
            for row_index,row in enumerate(self.energy_levels):
                for column_index,octopus_energy in enumerate(row):
                    self.energy_levels[row_index][column_index] += 1
        else:
            for position in positions:
                row_index,column_index = position
                self.energy_levels[row_index][column_index] += 1
        
    def check_flashers(self):
        """Find locations that are now eligible to flash"""
        ready = set()
        for row_index,row in enumerate(self.energy_levels):
            for column_index,octopus_energy in enumerate(row):
                if self.energy_levels[row_index][column_index] > 9:
                    ready.add((row_index,column_index))
        return ready

    def reset_flashed(self):
        """Reset positions in flashed list to zero ready for next round"""
        for position in self.flashed:
            x,y = position
            self.energy_levels[x][y] = 0

    def compute_next_step(self):
        self.increment(None)
        while True:
            ready_to_flash = self.check_flashers()
            if len(ready_to_flash) == 0:
                break
            else:
                for octopus in ready_to_flash:
                    self.process_flash(octopus)
                self.reset_flashed()
        self.total_flashes += len(self.flashed)
        if len(self.flashed) == len(self.energy_levels) * len(self.energy_levels[0]):
            self.synchro_flag = True
        self.flashed = set()


    def compute_steps(self,steps):
        for step in range(0,steps):
            self.compute_next_step()
            if self.synchro_flag == True:
                print(f'SYNCHRONISATION DURING STEP: {step+1}')
                self.synchro_flag = False

    def print_energy(self):
        print()
        for row in self.energy_levels:
            print(row)
        print()

    def read_input_file(self,filename):
        with open(filename,'r') as f:
            for line in f:
                self.energy_levels.append(list(line.strip()))
        for row_index,row in enumerate(self.energy_levels):
            for column_index,octopus_energy in enumerate(row):
                self.energy_levels[row_index][column_index] = int(self.energy_levels[row_index][column_index])

