from Packet import Packet

def main():
    input = read_input_file("Day16\DaySixteenTestInput")
    print(input)
    binary_packet = bin(int(input[0],16))
    binary_packet = binary_packet[2:]
    outer_packet = Packet(binary_packet)


def read_input_file(filename):
    input = []
    with open(filename,'r') as f:
        for line in f:
            input.append(line)
    return input

if __name__ == '__main__':
    main()
