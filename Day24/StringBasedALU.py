class StringALU:
    """ALU that builds strings describing the equations"""

    def __init__(self):
        self.w = '0'
        self.x = '0'
        self.y = '0'
        self.z = '0'
        self.model_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n']
        self.model_pointer = 0

    def handle_instruction(self, instruction_list):
        instruction = instruction_list[0]
        operand_a = instruction_list[1]
        if len(instruction_list) > 2:
            operand_b = instruction_list[2]
            self.process_instruction(instruction, operand_a, operand_b)
        else:
            self.process_instruction(instruction, operand_a)

    def process_instruction(self, instruction, operand_a, operand_b=None):
        if instruction == 'add':
            self.add(operand_a, operand_b)
        elif instruction == 'inp':
            self.inp(operand_a)
        elif instruction == 'mul':
            self.mul(operand_a, operand_b)
        elif instruction == 'div':
            self.div(operand_a, operand_b)
        elif instruction == 'mod':
            self.mod(operand_a, operand_b)
        elif instruction == 'eql':
            self.eql(operand_a, operand_b)

    def inp(self,operand_a):
        self.w = self.model_letters[self.model_pointer]
        self.model_pointer += 1

    def add(self,operand_a, operand_b):
        if operand_b == 'w':
            operand_b = self.w
        if operand_b == 'x':
            operand_b = self.x
        if operand_b == 'y':
            operand_b = self.y
        if operand_b == 'z':
            operand_b = self.z

        if operand_a == 'w':
            self.w = '(' + self.w + ')' + ' + ' + operand_b
        elif operand_a == 'x':
            self.x = '(' + self.x + ')' + ' + ' + operand_b
        elif operand_a == 'y':
            self.y = '(' + self.y + ')' + ' + ' + operand_b
        elif operand_a == 'z':
            self.z = '(' + self.z + ')' + ' + ' + operand_b


    def mul(self,operand_a, operand_b):
        if operand_b == 'w':
            operand_b = self.w
        if operand_b == 'x':
            operand_b = self.x
        if operand_b == 'y':
            operand_b = self.y
        if operand_b == 'z':
            operand_b = self.z

        if operand_a == 'w':
            self.w = '(' + self.w + ')' + ' x ' + operand_b
        elif operand_a == 'x':
            self.x = '(' + self.x + ')' + ' x ' + operand_b
        elif operand_a == 'y':
            self.y = '(' + self.y + ')' + ' x ' + operand_b
        elif operand_a == 'z':
            self.z = '(' + self.z + ')' + ' x ' + operand_b

    def div(self,operand_a, operand_b):
        if operand_b == 'w':
            operand_b = self.w
        if operand_b == 'x':
            operand_b = self.x
        if operand_b == 'y':
            operand_b = self.y
        if operand_b == 'z':
            operand_b = self.z

        if operand_a == 'w':
            self.w = '(' + self.w + ')' + ' / ' + operand_b
        elif operand_a == 'x':
            self.x = '(' + self.x + ')' + ' / ' + operand_b
        elif operand_a == 'y':
            self.y = '(' + self.y + ')' + ' / ' + operand_b
        elif operand_a == 'z':
            self.z = '(' + self.z + ')' + ' / ' + operand_b

    def mod(self,operand_a, operand_b):
        if operand_b == 'w':
            operand_b = self.w
        if operand_b == 'x':
            operand_b = self.x
        if operand_b == 'y':
            operand_b = self.y
        if operand_b == 'z':
            operand_b = self.z

        if operand_a == 'w':
            self.w = '(' + self.w + ')' + ' % ' + operand_b
        elif operand_a == 'x':
            self.x = '(' + self.x + ')' + ' % ' + operand_b
        elif operand_a == 'y':
            self.y = '(' + self.y + ')' + ' % ' + operand_b
        elif operand_a == 'z':
            self.z = '(' + self.z + ')' + ' % ' + operand_b
            
    def eql(self,operand_a, operand_b):
        if operand_b == 'w':
            operand_b = self.w
        elif operand_b == 'x':
            operand_b = self.x
        elif operand_b == 'y':
            operand_b = self.y
        elif operand_b == 'z':
            operand_b = self.z

        if operand_a == 'w':
            self.w = '1' if self.w == operand_b else '0'
        elif operand_a == 'x':
            self.x = '1' if self.x == operand_b else '0'
        elif operand_a == 'y':
            self.y = '1' if self.y == operand_b else '0'
        elif operand_a == 'z':
            self.z = '1' if self.z == operand_b else '0'