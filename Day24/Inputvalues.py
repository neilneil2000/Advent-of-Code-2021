class ALU:

    def __init__(self):
        self.w = { 0: { 'a' : {1,2,3,4,5,6,7,8,9},
            'b' : {1,2,3,4,5,6,7,8,9},
            'c' : {1,2,3,4,5,6,7,8,9},
            'd' : {1,2,3,4,5,6,7,8,9},
            'e' : {1,2,3,4,5,6,7,8,9},
            'f' : {1,2,3,4,5,6,7,8,9},
            'g' : {1,2,3,4,5,6,7,8,9},
            'h' : {1,2,3,4,5,6,7,8,9},
            'i' : {1,2,3,4,5,6,7,8,9},
            'j' : {1,2,3,4,5,6,7,8,9},
            'k' : {1,2,3,4,5,6,7,8,9},
            'l' : {1,2,3,4,5,6,7,8,9},
            'm' : {1,2,3,4,5,6,7,8,9},
            'n' : {1,2,3,4,5,6,7,8,9}
            }}
        self.x = { 0: { 'a' : {1,2,3,4,5,6,7,8,9},
            'b' : {1,2,3,4,5,6,7,8,9},
            'c' : {1,2,3,4,5,6,7,8,9},
            'd' : {1,2,3,4,5,6,7,8,9},
            'e' : {1,2,3,4,5,6,7,8,9},
            'f' : {1,2,3,4,5,6,7,8,9},
            'g' : {1,2,3,4,5,6,7,8,9},
            'h' : {1,2,3,4,5,6,7,8,9},
            'i' : {1,2,3,4,5,6,7,8,9},
            'j' : {1,2,3,4,5,6,7,8,9},
            'k' : {1,2,3,4,5,6,7,8,9},
            'l' : {1,2,3,4,5,6,7,8,9},
            'm' : {1,2,3,4,5,6,7,8,9},
            'n' : {1,2,3,4,5,6,7,8,9}
            }}
        self.y = { 0: { 'a' : {1,2,3,4,5,6,7,8,9},
            'b' : {1,2,3,4,5,6,7,8,9},
            'c' : {1,2,3,4,5,6,7,8,9},
            'd' : {1,2,3,4,5,6,7,8,9},
            'e' : {1,2,3,4,5,6,7,8,9},
            'f' : {1,2,3,4,5,6,7,8,9},
            'g' : {1,2,3,4,5,6,7,8,9},
            'h' : {1,2,3,4,5,6,7,8,9},
            'i' : {1,2,3,4,5,6,7,8,9},
            'j' : {1,2,3,4,5,6,7,8,9},
            'k' : {1,2,3,4,5,6,7,8,9},
            'l' : {1,2,3,4,5,6,7,8,9},
            'm' : {1,2,3,4,5,6,7,8,9},
            'n' : {1,2,3,4,5,6,7,8,9}
            }}
        self.z = { 0: { 'a' : {1,2,3,4,5,6,7,8,9},
            'b' : {1,2,3,4,5,6,7,8,9},
            'c' : {1,2,3,4,5,6,7,8,9},
            'd' : {1,2,3,4,5,6,7,8,9},
            'e' : {1,2,3,4,5,6,7,8,9},
            'f' : {1,2,3,4,5,6,7,8,9},
            'g' : {1,2,3,4,5,6,7,8,9},
            'h' : {1,2,3,4,5,6,7,8,9},
            'i' : {1,2,3,4,5,6,7,8,9},
            'j' : {1,2,3,4,5,6,7,8,9},
            'k' : {1,2,3,4,5,6,7,8,9},
            'l' : {1,2,3,4,5,6,7,8,9},
            'm' : {1,2,3,4,5,6,7,8,9},
            'n' : {1,2,3,4,5,6,7,8,9}
            }}
        self.model_numbers = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']

    def add(self, operand_a, operand_b):
        output = {}
        literal_flag = False

        literal_flag, operand_a = self.process_operand(operand_a)
        literal_flag, operand_b = self.process_operand(operand_b)
    
        if literal_flag == True: #Register + literal (no clashes possible)
            for a_value in operand_a:
                new_value = a_value + operand_b
                output.update({new_value: operand_a[a_value]})
        else: #Register + Register
            for a_value in operand_a:
                for b_value in operand_b:
                    new_value = a_value + b_value
                    possibles = {}
                    for letter in self.model_numbers:
                        letter_possibles = operand_a[a_value][letter].intersection(operand_b[b_value][letter])
                        possibles.update( { letter: letter_possibles } )
                    if new_value in output:
                        for letter in self.model_numbers:
                            letter_possibles = possibles[letter].union(output[new_value][letter])
                            possibles.update( { letter: letter_possibles } )
                    else:
                        output.update({new_value: possibles})

        #Assign Output
        if operand_a == self.w:
            self.w = output
        elif operand_a == self.x:
            self.x = output
        elif operand_a == self.y:
            self.y = output
        elif operand_a == self.z:
            self.z = output



    def mul(self, operand_a, operand_b):
        output = {}
        for current_value in operand_a:
            new_value = current_value * operand_b
            if new_value in output:
                for element in output[new_value]:
                    print(f'Need to handle this properly!')
                    print(element)
            else:
                output.update({new_value : operand_a[current_value]})
        

    def inp(self):
        #Assume inp is always w
        w = { 1: {'a' : {1}, 
            'b' : {1,2,3,4,5,6,7,8,9},
            'c' : {1,2,3,4,5,6,7,8,9},
            'd' : {1,2,3,4,5,6,7,8,9},
            'e' : {1,2,3,4,5,6,7,8,9},
            'f' : {1,2,3,4,5,6,7,8,9},
            'g' : {1,2,3,4,5,6,7,8,9},
            'h' : {1,2,3,4,5,6,7,8,9},
            'i' : {1,2,3,4,5,6,7,8,9},
            'j' : {1,2,3,4,5,6,7,8,9},
            'k' : {1,2,3,4,5,6,7,8,9},
            'l' : {1,2,3,4,5,6,7,8,9},
            'm' : {1,2,3,4,5,6,7,8,9},
            'n' : {1,2,3,4,5,6,7,8,9}},
            2: {'a' : {2}, 
            'b' : {1,2,3,4,5,6,7,8,9},
            'c' : {1,2,3,4,5,6,7,8,9},
            'd' : {1,2,3,4,5,6,7,8,9},
            'e' : {1,2,3,4,5,6,7,8,9},
            'f' : {1,2,3,4,5,6,7,8,9},
            'g' : {1,2,3,4,5,6,7,8,9},
            'h' : {1,2,3,4,5,6,7,8,9},
            'i' : {1,2,3,4,5,6,7,8,9},
            'j' : {1,2,3,4,5,6,7,8,9},
            'k' : {1,2,3,4,5,6,7,8,9},
            'l' : {1,2,3,4,5,6,7,8,9},
            'm' : {1,2,3,4,5,6,7,8,9},
            'n' : {1,2,3,4,5,6,7,8,9}},
            3: {'a' : {3}, 
            'b' : {1,2,3,4,5,6,7,8,9},
            'c' : {1,2,3,4,5,6,7,8,9},
            'd' : {1,2,3,4,5,6,7,8,9},
            'e' : {1,2,3,4,5,6,7,8,9},
            'f' : {1,2,3,4,5,6,7,8,9},
            'g' : {1,2,3,4,5,6,7,8,9},
            'h' : {1,2,3,4,5,6,7,8,9},
            'i' : {1,2,3,4,5,6,7,8,9},
            'j' : {1,2,3,4,5,6,7,8,9},
            'k' : {1,2,3,4,5,6,7,8,9},
            'l' : {1,2,3,4,5,6,7,8,9},
            'm' : {1,2,3,4,5,6,7,8,9},
            'n' : {1,2,3,4,5,6,7,8,9}},
            4: {'a' : {4}, 
            'b' : {1,2,3,4,5,6,7,8,9},
            'c' : {1,2,3,4,5,6,7,8,9},
            'd' : {1,2,3,4,5,6,7,8,9},
            'e' : {1,2,3,4,5,6,7,8,9},
            'f' : {1,2,3,4,5,6,7,8,9},
            'g' : {1,2,3,4,5,6,7,8,9},
            'h' : {1,2,3,4,5,6,7,8,9},
            'i' : {1,2,3,4,5,6,7,8,9},
            'j' : {1,2,3,4,5,6,7,8,9},
            'k' : {1,2,3,4,5,6,7,8,9},
            'l' : {1,2,3,4,5,6,7,8,9},
            'm' : {1,2,3,4,5,6,7,8,9},
            'n' : {1,2,3,4,5,6,7,8,9}},
            5: {'a' : {5}, 
            'b' : {1,2,3,4,5,6,7,8,9},
            'c' : {1,2,3,4,5,6,7,8,9},
            'd' : {1,2,3,4,5,6,7,8,9},
            'e' : {1,2,3,4,5,6,7,8,9},
            'f' : {1,2,3,4,5,6,7,8,9},
            'g' : {1,2,3,4,5,6,7,8,9},
            'h' : {1,2,3,4,5,6,7,8,9},
            'i' : {1,2,3,4,5,6,7,8,9},
            'j' : {1,2,3,4,5,6,7,8,9},
            'k' : {1,2,3,4,5,6,7,8,9},
            'l' : {1,2,3,4,5,6,7,8,9},
            'm' : {1,2,3,4,5,6,7,8,9},
            'n' : {1,2,3,4,5,6,7,8,9}},
            6: {'a' : {6}, 
            'b' : {1,2,3,4,5,6,7,8,9},
            'c' : {1,2,3,4,5,6,7,8,9},
            'd' : {1,2,3,4,5,6,7,8,9},
            'e' : {1,2,3,4,5,6,7,8,9},
            'f' : {1,2,3,4,5,6,7,8,9},
            'g' : {1,2,3,4,5,6,7,8,9},
            'h' : {1,2,3,4,5,6,7,8,9},
            'i' : {1,2,3,4,5,6,7,8,9},
            'j' : {1,2,3,4,5,6,7,8,9},
            'k' : {1,2,3,4,5,6,7,8,9},
            'l' : {1,2,3,4,5,6,7,8,9},
            'm' : {1,2,3,4,5,6,7,8,9},
            'n' : {1,2,3,4,5,6,7,8,9}},
            7: {'a' : {7}, 
            'b' : {1,2,3,4,5,6,7,8,9},
            'c' : {1,2,3,4,5,6,7,8,9},
            'd' : {1,2,3,4,5,6,7,8,9},
            'e' : {1,2,3,4,5,6,7,8,9},
            'f' : {1,2,3,4,5,6,7,8,9},
            'g' : {1,2,3,4,5,6,7,8,9},
            'h' : {1,2,3,4,5,6,7,8,9},
            'i' : {1,2,3,4,5,6,7,8,9},
            'j' : {1,2,3,4,5,6,7,8,9},
            'k' : {1,2,3,4,5,6,7,8,9},
            'l' : {1,2,3,4,5,6,7,8,9},
            'm' : {1,2,3,4,5,6,7,8,9},
            'n' : {1,2,3,4,5,6,7,8,9}},
            8: {'a' : {8}, 
            'b' : {1,2,3,4,5,6,7,8,9},
            'c' : {1,2,3,4,5,6,7,8,9},
            'd' : {1,2,3,4,5,6,7,8,9},
            'e' : {1,2,3,4,5,6,7,8,9},
            'f' : {1,2,3,4,5,6,7,8,9},
            'g' : {1,2,3,4,5,6,7,8,9},
            'h' : {1,2,3,4,5,6,7,8,9},
            'i' : {1,2,3,4,5,6,7,8,9},
            'j' : {1,2,3,4,5,6,7,8,9},
            'k' : {1,2,3,4,5,6,7,8,9},
            'l' : {1,2,3,4,5,6,7,8,9},
            'm' : {1,2,3,4,5,6,7,8,9},
            'n' : {1,2,3,4,5,6,7,8,9}},
            9: {'a' : {9}, 
            'b' : {1,2,3,4,5,6,7,8,9},
            'c' : {1,2,3,4,5,6,7,8,9},
            'd' : {1,2,3,4,5,6,7,8,9},
            'e' : {1,2,3,4,5,6,7,8,9},
            'f' : {1,2,3,4,5,6,7,8,9},
            'g' : {1,2,3,4,5,6,7,8,9},
            'h' : {1,2,3,4,5,6,7,8,9},
            'i' : {1,2,3,4,5,6,7,8,9},
            'j' : {1,2,3,4,5,6,7,8,9},
            'k' : {1,2,3,4,5,6,7,8,9},
            'l' : {1,2,3,4,5,6,7,8,9},
            'm' : {1,2,3,4,5,6,7,8,9},
            'n' : {1,2,3,4,5,6,7,8,9}}}
        self.w = w
        pass

    def process_operand(self, operand):
        """Takes an operand and returns the pointer to the relevant register or in the case of a literal, just itself"""
        literal_flag = False
        if operand == 'w':
            operand = self.w
        elif operand == 'x':
            operand = self.x
        elif operand == 'y':
            operand = self.y
        elif operand == 'z':
            operand = self.z
        else:
            operand = int(operand)
            literal_flag = True
        return literal_flag, operand

    def execute_instruction(self, instruction, operand_a, operand_b=None):
        operand_a = self.process_operand(operand_a)
        if operand_b is not None:
            operand_b = self.process_operand(operand_b)
        if instruction == instructions.inp:
            self.inp()
        elif instruction == instructions.mul:
            self.mul(operand_a, operand_b)
        elif instruction == instructions.add:
            self.add(operand_a, operand_b)
           


    def print_all_values(self):
        print(f'Possible values for w:')
        self.print_possible_values(self.w)
        print(f'Possible values for x:')
        self.print_possible_values(self.x)
        print(f'Possible values for y:')
        self.print_possible_values(self.y)
        print(f'Possible values for z:')
        self.print_possible_values(self.z)

    def print_possible_values(self, variable: dict):
        for value in variable.keys():
            print(f'Could be {value} if ALL of the following are true')
            for item in variable[value]:
                print(f'{item} is one of {variable[value][item]}')