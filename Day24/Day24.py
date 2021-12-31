from Inputvalues import ALU
import time

def main():
   my_ALU = ALU()
   instructions = read_input_file()
   print_registers(my_ALU)
   for instruction in instructions:
      print(f"Next Instruction: {' '.join(instruction)}\t\t{time.perf_counter()} : ",end="")
      if len(instruction) == 2:
         my_ALU.execute_instruction(instruction[0], instruction[1])
      else:
         my_ALU.execute_instruction(instruction[0], instruction[1], instruction[2])
      print(f" {time.perf_counter()}")
   #print_registers(my_ALU)
   print()
   print(f'z = 0 when ...')
   for letter in my_ALU.z[0]:
      print(f'{my_ALU.z[0][letter]}')
   pass

def print_registers(my_ALU):
   for value in my_ALU.w:
      print(f" w: {value} if a in {my_ALU.w[value]['a']} and b in {my_ALU.w[value]['b']} and c in {my_ALU.w[value]['c']}")
   for value in my_ALU.x:
      print(f" x: {value} if a in {my_ALU.x[value]['a']} and b in {my_ALU.x[value]['b']} and c in {my_ALU.x[value]['c']}")
   for value in my_ALU.y:
      print(f" y: {value} if a in {my_ALU.y[value]['a']} and b in {my_ALU.y[value]['b']} and c in {my_ALU.y[value]['c']}")
   for value in my_ALU.z:
      print(f" z: {value} if a in {my_ALU.z[value]['a']} and b in {my_ALU.z[value]['b']} and c in {my_ALU.z[value]['c']}")
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