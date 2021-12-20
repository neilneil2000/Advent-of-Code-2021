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

    #TYPES
    TYPE_SUM = 0
    TYPE_PRODUCT = 1
    TYPE_MINIMUM = 2
    TYPE_MAXIMUM = 3
    TYPE_LITERAL = 4
    TYPE_GREATER_THAN = 5
    TYPE_LESS_THAN = 6
    TYPE_EQUAL_TO = 7
        
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

    def calculate_sum(self):
        total = 0
        for packet in self.subpackets:
            total += packet.literal_value
        self.literal_value = total

    def calculate_product(self):
        total = 1
        for packet in self.subpackets:
            total *= packet.literal_value
        self.literal_value = total

    def calculate_minimum(self):
        literals = []
        for packet in self.subpackets:
            literals.append(packet.literal_value)
        self.literal_value = min(literals)

    def calculate_maximum(self):
        literals = []
        for packet in self.subpackets:
            literals.append(packet.literal_value)
        self.literal_value = max(literals)

    def calculate_greater_than(self):
        answer = 0
        a = self.subpackets[0].literal_value
        b = self.subpackets[1].literal_value
        if a > b:
            answer = 1
        self.literal_value = answer

    def calculate_less_than(self):
        answer = 0
        a = self.subpackets[0].literal_value
        b = self.subpackets[1].literal_value
        if a < b:
            answer = 1
        self.literal_value = answer

    def calculate_equal_to(self):
        answer = 0
        a = self.subpackets[0].literal_value
        b = self.subpackets[1].literal_value
        if a == b:
            answer = 1
        self.literal_value = answer
    
    def calculate_literal(self):
        for packet in self.subpackets:
            packet.calculate_literal() #cascade
        type = self.type
        if type == Packet.TYPE_SUM:
            self.calculate_sum()
        elif type == Packet.TYPE_PRODUCT:
            self.calculate_product()
        elif type == Packet.TYPE_MINIMUM:
            self.calculate_minimum()
        elif type == Packet.TYPE_MAXIMUM:
            self.calculate_maximum()
        elif type == Packet.TYPE_GREATER_THAN:
            self.calculate_greater_than()
        elif type == Packet.TYPE_LESS_THAN:
            self.calculate_less_than()
        elif type == Packet.TYPE_EQUAL_TO:
            self.calculate_equal_to()
        elif type == Packet.TYPE_LITERAL:
            pass
        else:
            print(f'Invalid Packet Type')


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
        self.literal_value = int(value_string,2)
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
        if self.type == Packet.TYPE_LITERAL:
            self.process_literal()
        else:
            self.process_operator()