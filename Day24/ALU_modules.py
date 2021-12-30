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
                

        