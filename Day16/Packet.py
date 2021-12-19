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
    ----------------------------------- ~ ~ ---------------   -----
    | VERSION |   TYPE  | N |  Value  |     |   |  Value  |   | 0 |
    ----------------------------------- ~ ~ --------------- ~ ----- ~> n 0s to make total body lengt divisible by 4
    |  X X X  |  1 0 0  | 1 | X X X X |     | 0 | X X X X |   | 0 |
    ----------------------------------- ~ ~ ---------------   -----

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
    OP_MODE_BITS_BITS = 15
    OP_MODE_PACKETS_BITS = 11

    KEEP_READING = 1
    LAST_DIGIT = 0
    LITERAL_DIGIT_LENGTH = 4

    def __init__(self,binary_string):
        self.header_string = binary_string[:Packet.HEADER_LENGTH]
        self.body_string = binary_string[Packet.HEADER_LENGTH:]
        self.version = int(self.header_string[:3],2)
        self.type = int(self.header_string[3:],2)
        self.pointer = 0
        self.process_packet()
    
    def process_literal(self):
        flag = Packet.KEEP_READING
        pointer = 0
        value_string = []
        while flag == Packet.KEEP_READING:
            flag = self.body_string[ pointer ]
            pointer += 1
            digit = self.body_string[ pointer : pointer + Packet.LITERAL_DIGIT_LENGTH ]
            value_string.append(int(digit))
        self.literal = int(value_string)

    def process_operator(self):
        op_bit = self.body_string[ self.pointer ]
        self.pointer += 1
        if op_bit == Packet.OP_MODE_BITS:
            bits = self.body_string[ self.pointer : Packet.OP_MODE_BITS_BITS + self.pointer ]
            self.pointer += Packet.OP_MODE_BITS_BITS
            length_of_packets = int(bits,2)
        else: #op_bit == Packet.OP_MODE_PACKETS
            bits = self.body_string[ self.pointer : Packet.OP_MODE_PACKETS_BITS + self.pointer ]
            self.pointer += Packet.OP_MODE_PACKETS_BITS
            number_of_packets = int(bits,2)
        pass


    def process_packet(self):
        if self.type == Packet.LITERAL_TYPE:
            self.process_literal()
        else:
            self.process_operator()