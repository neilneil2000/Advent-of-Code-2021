def main():

    input = read_input_file("Day18\DayEighteenInput")
    result = input[0]
    for index in range(1, len(input)):
        result = add(result,input[index])
        result = full_reduce(result)
    print(result)
    while result[0] == '[':
        result = next_magnitude(result)
    print(result)

    #Refresh Input
    input = read_input_file("Day18\DayEighteenInput")
    magnitudes = {}
    for i in range(0,len(input)):
        for j in range(0, len(input)):
            if i !=j:
                m = add(input[i],input[j])
                m = full_reduce(m)
                while m[0] == '[':
                    m = next_magnitude(m)
                magnitudes.update({(i,j):int(m)})

    biggest = max(magnitudes.values())
    print(biggest)



    

def read_input_file(filename):
    numbers = []
    with open(filename,'r') as f:
        for line in f:
            numbers.append(line.strip())
    return numbers


def add(a: str, b: str) -> str:
    """Adds two snailfish numbers together (represented by strings)"""
    return '[' + str(a) +',' + str(b) + ']'

def full_reduce(a):
    b = None
    #print("Starting Reduction Loop")
    #print(a)
    while a != b:
        result = reduce_once(a)
        #print(result)
        b = a
        a = result
    #print("No further reduction possible")
    return a


def reduce_once(a):
    """ Reduce a snailfish number to its final form"""
    # Search for 5 deep brackets
    bracket_counter = 0
    digit_counter = 0
    done_flag = False
    for i,char in enumerate(a):
        if char == '[':
            bracket_counter += 1
            digit_counter = 0
        elif char == ']':
            bracket_counter -= 1
            digit_counter = 0
        if bracket_counter == 5:
            a = explode(a)
            done_flag = True
            break

    if done_flag == False:
        non_numeric = { '[', ']', ',' }
        for i,char in enumerate(a):
            if char in non_numeric: 
                digit_counter = 0
            else:
                digit_counter += 1
        
            if digit_counter == 2:
                a = split(a)
                break
        #DANGER - could go over 99 -> Need to improve split method to handle more than two digits
    
    return a
        
def next_magnitude(a: str) -> str:
    open  = {'['}
    close = {']'}
    comma = {','}
    number = {'0','1','2','3','4','5','6','7','8','9'}
    looking_for = open
    second = False # True if looking for second number in a pair
    start = None
    end  = None
    for i, char in enumerate(a):
        if char in open:
            start = i
        if char in looking_for:
            if char in open:
                looking_for = number
            elif char in comma: 
                looking_for = number
                second = True
            elif char in number:
                if second == True:
                    looking_for = number
                    looking_for = looking_for.union(close)
                    second = False
                else:
                    looking_for = looking_for.union(comma)
            elif char in close:
                end = i + 1
                break
        else:
            second = False
            if char in open:
                looking_for = number
            else:
                looking_for = open
            
    m = magnitude(a[start:end])

    result = a[:start] + str(m) + a[end:]
    return result
    
            
            



def magnitude(a: str) -> int:

    a = a[1:-1].split(',')
    a[0] = int(a[0])*3
    a[1] = int(a[1])*2
    a = sum(a)
    return a

def explode(a: str) -> str:
    result = a
    depth_counter = 0
    #Step through number until you find the first set nested in 4 layers then explode that location using string slicing
    for i, char in enumerate(a):
        if char =='[':
            depth_counter += 1
        elif char == ']':
            depth_counter -= 1
        if depth_counter == 5:
            break
    left = a[:i]
    working_string = a[i:]
    for i, char in enumerate(working_string):
        if char == ']':
            break
    value_to_explode = working_string[1:i]
    value_to_explode = value_to_explode.split(',')
    right = working_string[i + 1:]
    #print(f'{left} <-- LEFT')
    #print(f'{value_to_explode} <-- VALUE TO EXPLODE')
    #print(f'{right} <-- RIGHT')

    #Find leftmost value in RIGHT
    right_exists = False
    right_pointer = None
    right_length = 1
    non_numeric = { '[', ']', ',' }
    for i, char in enumerate(right):
        if char not in non_numeric:
            right_exists = True
            right_pointer = i
            break
    if right_exists is True:
        for i, char in enumerate(right[i+1:]):
            if char in non_numeric:
                right_length += i
                break

        
    if right_exists is True:
        left_of_right = right[:right_pointer]
        right_value = int(right[right_pointer:right_pointer + right_length])
        right_of_right = right[right_pointer + right_length:]
        #print(f'Right Value = {right_value}')
        right_value = right_value + int(value_to_explode[1])
        #print(f'New right Value = {right_value}')
        right = left_of_right + str(right_value) + right_of_right
    
    #Find rightmost value in LEFT
    left_exists = False
    left_pointer = None
    left_length = 1
    for i in range(len(left)-1, -1, -1):
        if left[i] not in non_numeric:
            left_exists = True
            left_pointer = i 
            break
    if left_exists is True:
        for i in range(len(left[:left_pointer-1]), -1 ,-1):
            if left[i] not in non_numeric:
                left_length += 1
                left_pointer -= 1
            else:
                break

    if left_exists is True:
        left_of_left = left[:left_pointer]
        left_value = int(left[left_pointer:left_pointer + left_length])
        right_of_left = left[left_pointer + left_length:]
        #print(f'Left Value = {left_value}')
        left_value = left_value + int(value_to_explode[0])
        #print(f'New left Value = {left_value}')
        left = left_of_left + str(left_value) + right_of_left

    #Join back together, replacing the exploded value with '0'
    result = left + '0' + right

    return result

def split(a: str) -> str:
    #Find first double digit in string
    digit_counter = 0
    non_numeric = { '[', ']', ',' }
    for i,char in enumerate(a):
        if char not in non_numeric:
            digit_counter += 1
        elif digit_counter > 0:
            digit_counter -= 1
        if digit_counter == 2:
            break
    pointer = i - 1
    value = int(a[ pointer : pointer + 2 ])
    left = a[ : pointer ]
    right = a[ pointer + 2: ]

    new_value = [int(value/2), int(value/2)+(value%2)]

    result = left + '[' + str(new_value[0]) + ',' + str(new_value[1]) + ']' + right
    return result

if __name__ == '__main__':
    main()