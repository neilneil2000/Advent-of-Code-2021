from typing import NoReturn


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
        self.model_number_pointer = 0

    def arithmetic_op(self, instruction: str, operand_a: int, operand_b: int) -> int:
        if instruction == 'add':
            result = operand_a + operand_b
        elif instruction == 'mul':
            result = operand_a * operand_b
        elif instruction == 'div':
            result = int(operand_a / operand_b)
        elif instruction == 'mod':
            result = operand_a % operand_b
        else:
            print(f'UNKNOWN INSTRUCTION')
        return result

    def arithmetic(self, instruction: str, operand_a: str, operand_b: str) -> None:
        output = {}
        literal_flag = False

        literal_flag, operand_a = self.process_operand(operand_a)
        literal_flag, operand_b = self.process_operand(operand_b) #Overwrite literal_flag as operand_a is never a literal
    
        if literal_flag == True: #Register + literal
            for a_value in operand_a:
                new_value = self.arithmetic_op(instruction, a_value, operand_b)
                possibles = {}
                for letter in self.model_numbers:
                        letter_possibles = operand_a[a_value][letter]
                        possibles.update( { letter: letter_possibles } )
                if new_value in output:
                    for letter in self.model_numbers:
                        letter_possibles = operand_a [a_value][letter].union(output[new_value][letter])
                        possibles.update( { letter: letter_possibles } )
                    output.update( { new_value: possibles} )
                else:
                    output.update({new_value: possibles})
        else: #Register + Register
            for a_value in operand_a:
                for b_value in operand_b:
                    #Check that there are some model number values that would satisfy this
                    overlap = True
                    for letter in self.model_numbers:
                        if len(operand_a[a_value][letter].intersection(operand_b[b_value][letter])) == 0:
                            overlap = False
                    if overlap == True:
                        new_value = self.arithmetic_op(instruction, a_value, b_value)
                        possibles = {}
                        for letter in self.model_numbers:
                            letter_possibles = operand_a[a_value][letter].intersection(operand_b[b_value][letter])
                            possibles.update( { letter: letter_possibles } )
                        if new_value in output:
                            for letter in self.model_numbers:
                                letter_possibles = possibles[letter].union(output[new_value][letter])
                                possibles.update( { letter: letter_possibles } )
                            output.update( { new_value: possibles} )
                        else:
                            output.update({new_value: possibles})

        #Assign Output
        if id(operand_a) == id(self.w):
            self.w = output
        elif id(operand_a) == id(self.x):
            self.x = output
        elif id(operand_a) == id(self.y):
            self.y = output
        elif id(operand_a) == id(self.z):
            self.z = output

    def equal(self, operand_a: str, operand_b: str) -> None:
        output = {}
        literal_flag = False

        literal_flag, operand_a = self.process_operand(operand_a)
        literal_flag, operand_b = self.process_operand(operand_b)
    
        if literal_flag == True:
            for a_value in operand_a:
                if a_value == operand_b:
                    new_value = 1
                else:
                    new_value = 0
                output.update( { new_value: operand_a [ a_value ] } )
        else:
            for a_value in operand_a:
                for b_value in operand_b:
                    #Check that there are some model number values that would satisfy this
                    overlap = True
                    for letter in self.model_numbers:
                        if len(operand_a[a_value][letter].intersection(operand_b[b_value][letter])) == 0:
                            overlap = False
                    if overlap == True:
                        if a_value == b_value:
                            new_value = 1
                        else:
                            new_value = 0
                        possibles = {}
                        for letter in self.model_numbers:
                            letter_possibles = operand_a[a_value][letter].intersection(operand_b[b_value][letter])
                            possibles.update( { letter: letter_possibles } )
                        if new_value in output:
                            for letter in self.model_numbers:
                                letter_possibles = possibles[letter].union(output[new_value][letter])
                                possibles.update( { letter: letter_possibles } )
                            output.update( { new_value: possibles} )
                        else:
                            output.update( { new_value: possibles } )
        #Assign Output
        if id(operand_a) == id(self.w):
            self.w = output
        elif id(operand_a) == id(self.x):
            self.x = output
        elif id(operand_a) == id(self.y):
            self.y = output
        elif id(operand_a) == id(self.z):
            self.z = output
                    
    def inp(self):
        #Assume inp is always w
        w = { 1: {'a' : {1,2,3,4,5,6,7,8,9}, 
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
            2: {'a' : {1,2,3,4,5,6,7,8,9}, 
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
            3: {'a' : {1,2,3,4,5,6,7,8,9}, 
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
            4: {'a' : {1,2,3,4,5,6,7,8,9}, 
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
            5: {'a' : {1,2,3,4,5,6,7,8,9}, 
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
            6: {'a' : {1,2,3,4,5,6,7,8,9}, 
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
            7: {'a' : {1,2,3,4,5,6,7,8,9}, 
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
            8: {'a' : {1,2,3,4,5,6,7,8,9}, 
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
            9: {'a' : {1,2,3,4,5,6,7,8,9}, 
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
        for number in w:
            w[number].update({ self.model_numbers[self.model_number_pointer] : {number} })
        self.model_number_pointer += 1
        self.w = w

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

    def execute_instruction(self, instruction: str, operand_a: str, operand_b = None):
        if instruction == 'inp':
            self.inp()
        elif instruction == 'eql':
            self.equal(operand_a, operand_b)
        else:
            self.arithmetic(instruction, operand_a, operand_b)
           


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
