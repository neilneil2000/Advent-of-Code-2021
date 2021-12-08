class SevenSegment:
    """
    Model Seven Segment Display with each segment an index in self.segments

        0000
       1    2
       1    2
        3333
       4    5
       4    5
        6666

    """
    input_wires = {'a','b','c','d','e','f','g'}
    zero = {0,1,2,4,5,6} # missing 3
    one = {2,5} #len 2
    two = {0,2,3,4,6}
    three = {0,2,3,5,6}
    four = {1,2,3,5} #len 4
    five = {0,1,3,5,6}
    six = {0,1,3,4,5,6} # missing 2
    seven = {0,2,5} # len 3
    eight = {0,1,2,3,4,5,6} #len 7
    nine = {0,1,2,3,5,6} # missing 4
    six_longs = {2,3,4}
    char_wires = [zero,one,two,three,four,five,six,seven,eight,nine,six_longs]
    

    
    def __init__(self):
        self.segments=[]
        for x in range(0,7):
            self.segments.append(SevenSegment.input_wires.copy())

    def decode_symbol(self,code_character):
        code_length = len(code_character)
        if code_length == 2:
            return 1
        elif code_length == 3:
            return 7
        elif code_length == 4:
            return 4
        elif code_length == 7:
            return 8
        else:
            code_character = list(code_character)
            character = set()
        for letter in code_character:
            for x in range(0,7):
                if letter in self.segments[x]:
                    character.add(x)
                    break
        for x in range(0,10):
            if character == SevenSegment.char_wires[x]:
                return x
            

    def decode(self,code_entry):
        multiplier = 1000
        code_value = 0
        for code_character in code_entry:
            code_value += multiplier * self.decode_symbol(code_character)
            multiplier /= 10
        return int(code_value)


    def check_six_lengths(self,clues):
        wires = set()
        for clue in clues:
            clue = list(clue)
            missing_wire = SevenSegment.input_wires.copy()
            missing_wire.difference_update(clue)
            wires = wires.union(missing_wire)
        self.set_wires(wires,10)
        
        #compare missing letters to six_longs

    
    def process_clue(self,wires):
        no_of_wires = len(wires)
        if no_of_wires == 2:
            self.set_wires(wires,1)
        elif no_of_wires ==3:
            self.set_wires(wires,7)
        elif no_of_wires == 4:
            self.set_wires(wires,4)
        self.check_singletons()

    def check_singletons(self):
        for x in range(0,7):
            if len(self.segments[x]) == 1:
                for y in range (0,7):
                    if x != y:
                        self.segments[y].difference_update(self.segments[x])
                    

    def set_wires(self,wires,number):
        wires = set(wires)
        inverse_wires = SevenSegment.input_wires.copy()
        inverse_wires.difference_update(wires)
        for x in range(0,7):
            if x in SevenSegment.char_wires[number]:
                self.segments[x].difference_update(inverse_wires)
            else:
                self.segments[x].difference_update(wires)


    def confirm_segment(self,wire,segment):
        for x in range(0,7):
            if x == segment:
                self.segments[x] = {wire}
            else:
                self.segments[x].remove(wire)
    
    def confirm_not_segment(self,wire,segment):
        self.segments[segment].remove(wire)


    def maybe_segment(self,wires,segment):
        not_wires = SevenSegment.input_wires.copy()
        for wire in wires:
            not_wires.remove(wire)
        for wire in not_wires:
            self.segments[segment].remove(wire)
    
    def is_solved(self):
        for segment in self.segments:
            if len(segment) != 1:
                return False
        return True
        