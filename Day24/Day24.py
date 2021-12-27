from Inputvalues import ALU,instructions
from enum import Enum

def main():
   my_ALU = ALU()
   #my_ALU.print_all_values()
   my_ALU.execute_instruction(instructions.inp, 'w')
   #my_ALU.print_all_values()
   my_ALU.execute_instruction(instructions.mul, 'x', 0)
   my_ALU.print_all_values()
   my_ALU.execute_instruction(instructions.add, 'x', 'z')


if __name__ == '__main__':
    main()