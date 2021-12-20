from os import get_inheritable


class Packet:
    """
    <----- HEADER ----->
    --------------------
    | VERSION |  TYPE  |
    -------------------- ----->
    |  3 bits | 3 bits |
    -------------------- 
    
                          LITERAL  PACKET 
    <----- HEADER -----><------------------ BODY ------------------->
    ----------------------------------- ~ ~ --------------- ~ -----
    | VERSION |   TYPE  | N |  Value  |     |   |  Value  |   | 0 |
    ----------------------------------- ~ ~ --------------- ~ ----- ~> n 0s to make total body length divisible by 4
    |  X X X  |  1 0 0  | 1 | X X X X |     | 0 | X X X X |   | 0 |
    ----------------------------------- ~ ~ --------------- ~ -----

                          OPERATOR  PACKET 
    <----- HEADER -----><------------------ BODY ------------------->
    ----------------------------------- ~ ~ ---------------
    | VERSION |   TYPE  |   |  Value  |     |   |  Value  |
    ----------------------------------- ~ ~ --------------- ~ ~> n 0s to make Body divisible by 4
    |  X X X  |  X X X  | 1 | X X X X |     | 0 | X X X X |
    ----------------------------------- ~ ~ ---------------

    """
    HEADER_LENGTH = 6
    VERSION_LENGTH = 3
    TYPE_LENGTH = 3
    LITERAL_TYPE = 4
    OP_MODE_BITS = '0'
    OP_MODE_PACKETS = '1'
    OP_MODE_BITS_LENGTH = 15
    OP_MODE_PACKETS_LENGTH = 11

    KEEP_READING = '1'
    LAST_DIGIT = '0'
    LITERAL_DIGIT_LENGTH = 4

    def __init__(self,binary_string):
    
        self.header_string = binary_string[:Packet.HEADER_LENGTH]
        self.body_string = binary_string[Packet.HEADER_LENGTH:]
        self.version = int(self.header_string[:3],2)
        self.type = int(self.header_string[3:],2)
        self.literal_value = None
        self.subpackets = []
        self.length = None
        self.process_packet()
    


    def get_total_version(self):
        total_version = 0
        for packet in self.subpackets:
            total_version += packet.get_total_version()
        total_version += self.version
        return total_version

    def get_length(self):
        return len(self.body_string) + len(self.header_string)

    def process_literal(self):
        flag = Packet.KEEP_READING
        pointer = 0
        value_string = ''
        while flag == Packet.KEEP_READING:
            flag = self.body_string[ pointer ]
            pointer += 1
            digit = self.body_string[ pointer : pointer + Packet.LITERAL_DIGIT_LENGTH ]
            pointer += Packet.LITERAL_DIGIT_LENGTH
            value_string += digit
        self.literal = int(value_string,2)
        self.body_string = self.body_string[:pointer]

    def process_operator(self):
        pointer = 0
        length_type_id = self.body_string[pointer]
        pointer += 1
        if length_type_id == Packet.OP_MODE_BITS:
            bits = self.body_string[ pointer : Packet.OP_MODE_BITS_LENGTH + pointer ]
            pointer += Packet.OP_MODE_BITS_LENGTH
            remaining_bits = int(bits,2)
            while remaining_bits > 0:
                self.subpackets.append(Packet(self.body_string[pointer:]))
                length = self.subpackets[-1].get_length()
                pointer += length
                remaining_bits -= length         
        else: #op_bit == Packet.OP_MODE_PACKETS
            packets = self.body_string[ pointer : Packet.OP_MODE_PACKETS_LENGTH + pointer ]
            pointer += Packet.OP_MODE_PACKETS_LENGTH
            number_of_packets = int(packets,2)
            for _ in range(0,number_of_packets):
                self.subpackets.append(Packet(self.body_string[pointer:]))
                pointer += self.subpackets[-1].get_length()
        self.body_string = self.body_string[:pointer]



    def process_packet(self):
        if self.type == Packet.LITERAL_TYPE:
            self.process_literal()
        else:
            self.process_operator()