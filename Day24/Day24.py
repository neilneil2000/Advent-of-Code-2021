from Inputvalues import ALU

def main():
   my_ALU = ALU()
   instructions = read_input_file()
   my_ALU.add('w','x')
   pass

def print_registers(my_ALU):
   print(f'w is {my_ALU.w}')
   print(f'x is {my_ALU.x}')
   print(f'y is {my_ALU.y}')
   print(f'z is {my_ALU.z}')
   print()


def read_input_file():
   input = []
   with open("Day24\DayTwentyFourInput", 'r') as f:
      for line in f:
         line = line.strip()
         line = line.split(' ')
         input.append(line)
   return input



if __name__ == '__main__':
    main()