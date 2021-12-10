class Subsystem:

    openers = ['(', '[', '{', '<']
    closers = [')', ']', '}', '>']
    corrupt_values = {')':3, ']':57, '}':1197, '>':25137}
    
    def __init__(self,filename):
        self.data = []
        self.backlog = []
        self.read_input_file(filename)
        self.corrupted = []
        self.corrupt_value = 0
        self.incompletion_values = []

    def calc_incompletion_value(self):
        self.incompletion_values.sort()
        index = int((len(self.incompletion_values)-1) / 2)
        return self.incompletion_values[index]

    def build_valid_options(self):
        valid = []
        valid.extend(Subsystem.openers)
        if len(self.backlog) > 0:
            index = Subsystem.openers.index(self.backlog[-1])
            valid.append(Subsystem.closers[index])
        return valid

    def calc_corruption_value(self):
        for bracket in self.corrupted:
            self.corrupt_value += self.corrupt_values[bracket]

    def calc_completion_value(self):
        value = 0
        while len(self.backlog) >0:
            bracket = self.backlog.pop()
            bracket_value = Subsystem.openers.index(bracket) + 1
            value *= 5
            value += bracket_value
        self.incompletion_values.append(value)


    def check_data(self):
        for row in self.data:
            self.backlog = []
            incorrect_bracket = self.is_row_corrupted(row)
            if incorrect_bracket is None:
                self.calc_completion_value()
            else:
                self.corrupted.append(incorrect_bracket)


    def is_row_corrupted(self,row):
        """ Checks whether given row is corrupted"""
        for bracket in row:
            valid = self.build_valid_options()
            if bracket not in valid:
                return bracket
            if bracket in Subsystem.openers:
                self.backlog.append(bracket)
            else:
                self.backlog.pop()
        return None

    def read_input_file(self,filename):
        with open(filename,'r') as f:
            for line in f:
                self.data.append(list(line.strip()))
