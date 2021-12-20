def main():
    algorithm, image = read_input_file("Day20\DayTwentyInput")
    print('ORIGINAL IMAGE')
    print('==============')
    for row in image:
        print(''.join(row))
    print()
    background_character = '.'
    for i in range(1,51):
        image = apply_algorithm(algorithm, image,background_character)
        #print(f' STEP {i} IMAGE')
        #print('==============')
        #for row in image:
        #    print(''.join(row))
        #print()
        if background_character  == '.':
            background_character = algorithm[0]
        else:
            background_character = algorithm[511]


    count = 0
    for row in image:
        count += row.count('#')
    print(count)

    for row in image:
        print(''.join(row))

def build_pixel_string(x,y,image,default):
    pixel_string = []
    if y > 0 and x > 0:
        pixel_string.append(image[y-1][x-1])
    else:
        pixel_string.append(default)
    if y > 0 and x > -1 and x < len(image[0]):
        pixel_string.append(image[y-1][x])
    else:
        pixel_string.append(default)
    if y > 0 and x < len(image[0])-1:
        pixel_string.append(image[y-1][x+1])
    else:
        pixel_string.append(default)
    if x > 0 and y > -1 and y < len(image):
        pixel_string.append(image[y][x-1])
    else:
        pixel_string.append(default)
    if x > -1 and x < len(image[0]) and y > -1 and y < len(image):
        pixel_string.append(image[y][x])
    else:
        pixel_string.append(default)
    if y > -1 and y < len(image) and x < len(image[0])-1:
        pixel_string.append(image[y][x+1])
    else:
        pixel_string.append(default)
    if y < len(image) - 1 and x > 0:
        pixel_string.append(image[y+1][x-1])
    else:
        pixel_string.append(default)
    if y < len(image) - 1 and x > -1 and x < len(image[0]):
        pixel_string.append(image[y+1][x])
    else:
        pixel_string.append(default)
    if y < len(image) - 1 and x < len(image[0]) -1:
        pixel_string.append(image[y+1][x+1])
    else:
        pixel_string.append(default)
    return pixel_string

def binary_to_decimal(binary):
    index = int(binary, 2)
    return index

def convert_pixels_to_binary(pixels):
    binary = []
    for pixel in pixels:
        if pixel == '#':
            binary.append('1')
        else:
            binary.append('0')
    return ''.join(binary)


def apply_algorithm(algorithm, image, default):
    new_image = []
    for y in range(-1,len(image)+1):
        new_image_row = []
        for x in range(-1,len(image[0])+1):
            pixels = build_pixel_string(x,y,image,default)
            binary = convert_pixels_to_binary(pixels)
            index = binary_to_decimal(binary)
            new_image_row.append(algorithm[index])
        new_image.append(new_image_row)

    return new_image
            
            


def read_input_file(filename):
    image = []
    with open(filename, 'r') as f:
        algorithm = f.readline().strip()
        f.readline()
        for line in f:
            image.append(line.strip())
    return algorithm, image




if __name__ == '__main__':
    main()