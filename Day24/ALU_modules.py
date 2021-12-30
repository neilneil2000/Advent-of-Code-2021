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

        



    def method_one(self):
        """output = trunc(input/divisor) IF mod in {1-9}"""
        if self.add_to_modulus > max(ModelDigit.VALID_DIGITS):
            return #If there can never be a match, then this method path will never be used
        for z in self.valid_inputs:
            if self.divide_by_26 == True:
                z = int(z/26)
            self.valid_outputs.add(z)
            
    
    def method_two(self):
        """output = 26trunc(input/divisor) + model_digit + add2 IF mod NOT in {1-9}"""
        for z in self.valid_inputs:
            z_out = z
            if self.divide_by_26 == True:
                z_out = int(z/26)
            z_out *= 26
            z_out += self.add_to_output
            for model_digit in range(9,0,-1):
                if (z % 26) + self.add_to_modulus != model_digit: #This would mean it would take the other path
                    self.valid_outputs.add(z_out+model_digit)

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







    def reverse_method_one(self):
        """output = trunc(input/divisor) IF mod in {1-9}"""
        if self.divide_by_26 == False:
            for output in self.target_outputs:
                if output % 26 + self.add_to_modulus in ModelDigit.VALID_DIGITS:
                    self.valid_inputs.add(output)
        else:
            for output in self.target_outputs:
                input = output * 26
                input_range = set()
                for i in range(0,26):
                    input_range.add(input + i)
                for input in input_range:
                    if input % 26 + self.add_to_modulus in ModelDigit.VALID_DIGITS:
                        self.valid_inputs.add(input)
                

    def reverse_method_two(self):
        """output = 26trunc(input/divisor) + model_digit + add2 IF mod NOT in {1-9}"""
        if self.divide_by_26 == False:
            for output in self.target_outputs:
                for digit_value in range(9,0,-1):
                    possible_input = output - digit_value - self.add_to_output
                    if possible_input % 26 + self.add_to_modulus != digit_value:
                        self.valid_inputs.add(possible_input)
        else:
            for output in self.target_outputs:
                for digit_value in range(9,0,-1):
                    possible_input = output - digit_value - self.add_to_output
                    if possible_input % 26 == 0:
                        possible_input = int(possible_input/26)
                        input_range = set()
                        for i in range(0,26):
                            input_range.add(possible_input + i)
                        for input in input_range:
                            if input % 26 + self.add_to_modulus in ModelDigit.VALID_DIGITS:
                                self.valid_inputs.add(input)
                            elif output - self.add_to_output in ModelDigit.VALID_DIGITS:
                                self.valid_inputs.add(input)