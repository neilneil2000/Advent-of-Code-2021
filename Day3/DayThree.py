def main():
    input = read_from_file("DayThreeInput")
    gamma, epsilon = calculate_power_parameters(input)
    power = gamma * epsilon
    print("DAY 3 PART 1 RESULT")
    print("===================")
    print("Power: " + str(power))
    oxygen,carbon_dioxide = calculate_life_support_parameters(input)
    life_support = oxygen * carbon_dioxide
    print("DAY 3 PART 2 RESULT")
    print("===================")
    print("Life Support: " + str(life_support))

def calculate_life_support_parameters(data):
    oxygen = list(data)
    for bit in range(0,len(oxygen[0])):
        keep_value = ones_vs_zeroes(oxygen,bit)
        remove_unwanted(oxygen,bit,keep_value)
    carbon_dioxide = list(data)
    for bit in range(0,len(carbon_dioxide[0])):
        delete_value = ones_vs_zeroes(carbon_dioxide,bit)
        if delete_value == 1:
            keep_value = 0
        else:
            keep_value = 1
        if len(carbon_dioxide) > 1:
            remove_unwanted(carbon_dioxide,bit,keep_value)
    oxygen = binary_list_to_decimal(oxygen[0])
    carbon_dioxide = binary_list_to_decimal(carbon_dioxide[0])
    return oxygen,carbon_dioxide
    

def remove_unwanted(data,bit,keep_value):
    """
    Remove all entries in data list that don't have keep_value at bit position (from left)
    """
    row = 0
    while True:
        if row >= len(data):
            break
        if int(data[row][bit]) != keep_value:
            del data[row]
        else:
            row += 1
    return data


def ones_vs_zeroes(data,bit):
    """
    Compares number of ones and zeroes in a given bit position
    Returns 1 if there are an equal number of 0 and 1 otherwise returns whichever there are more of
    """
    ones = 0
    for item in data:
            if item[bit] == '1' or item[bit] == 1:
                ones += 1
    if ones >= len(data) / 2:
        return 1
    else:
        return 0
    

def calculate_power_parameters(data):
    gamma = []
    epsilon = []
    value_length = len(data[0])
    for bit in range(0,value_length):
        value = ones_vs_zeroes(data,bit)
        gamma.append(value)
        if value == 0:
            epsilon.append(1)
        else:
            epsilon.append(0)
    gamma = binary_list_to_decimal(gamma)
    epsilon = binary_list_to_decimal(epsilon)
    return gamma, epsilon

def binary_list_to_decimal(binary_list):
    decimal = 0
    number_of_bits = len(binary_list)
    place_value = 2**(number_of_bits-1)
    for bit in binary_list:
        decimal += int(bit) * place_value
        place_value = int (place_value / 2)
    return decimal


def read_from_file(filename):
    f = open(filename, 'r')
    line_number = 0
    data =[]
    while True:
        line_number += 1
        line = f.readline()
        if not line:
            break    
        value = line.strip()
        data.append(list(value))
    f.close()
    return data

if __name__ == '__main__':
    main()