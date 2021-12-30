class ModelDigit:

    VALID_DIGITS = {1,2,3,4,5,6,7,8,9}

    def __init__(self, divide: bool, add1: int, add2: int):
        self.divide_by_26 = divide
        self.add_to_modulus = add1
        self.add_to_output = add2
        self.valid_inputs = set()
        self.valid_outputs = set()
        self.target_outputs = set()

    def set_inputs(self, inputs):
        self.valid_inputs = set()
        for input in inputs:
            self.valid_inputs.add(input)

    def set_outputs(self, outputs):
        self.target_outputs = set()
        for output in outputs:
            self.target_outputs.add(output)

    def attempt(self, model_digit, z_input):
        z = z_input
        if self.divide_by_26==True:
                z = int(z_input/26)
        if z_input % 26 + self.add_to_modulus != model_digit:
            z *= 26
            z += model_digit + self.add_to_output
        return z

    def calculate_valid_inputs(self):
        """There are two possible scenarios in two types"""
        if self.divide_by_26 == False:
            possible_inputs = self.target_outputs.copy() #Scenario 1: z_out = z_in
            for output in self.target_outputs:
                for digit_value in range(9,0,-1):
                    interim_value = output - digit_value - self.add_to_output
                    if interim_value >= 0:
                        if interim_value % 26 == 0:
                            input = int(interim_value/26)
                            possible_inputs.add(input) #Scenario 2: z_out = 26z_in + digit_value + output_add

        else: #self.divide_by_26 == True:
            possible_inputs = set()
            for output in self.target_outputs:
                output *= 26
                for i in range(0,26):
                    possible_inputs.add(output + i) #Scenario 1: z_out = trunc(z_in/26)
            for output in self.target_outputs:
                for digit_value in range(9,0,-1):
                    interim_value = output - digit_value - self.add_to_output
                    if interim_value >= 0:
                        if interim_value % 26 == 0:
                            input = int(interim_value/26)
                            for i in range(0,26):
                                possible_inputs.add(input + i) #Scenario 2: z_out = 26trunc(z_in/26) + digit_value + output_add

        #Validate the possible values
        for input in possible_inputs:
            for digit_value in range(9,0,-1):
                if self.attempt(digit_value, input) in self.target_outputs:
                    self.valid_inputs.add(input)