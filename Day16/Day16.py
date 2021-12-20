from Packet import Packet

def main():
    input = read_input_file("Day16\DaySixteenInput")
    print(input)
    binary_string = bin(int(input[0],16))
    binary_string = binary_string[2:] #Remove '0b' from front
    preceeding_zeroes = 4 - (len(binary_string) % 4)
    if preceeding_zeroes == 4:
        preceeding_zeroes = 0
    for _ in range(0, preceeding_zeroes):
        binary_string = '0' + binary_string
    outer_packet = Packet(binary_string)
    total_version = outer_packet.get_total_version()
    print(f'Sum of Version Numbers: {total_version}')
    print(f'END')


def read_input_file(filename):
    input = []
    with open(filename,'r') as f:
        for line in f:
            input.append(line.strip())
    return input

if __name__ == '__main__':
    main()
