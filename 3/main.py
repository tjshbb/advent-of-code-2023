#global variables
schematic_array = []
sum_of_parts = 0

def find_full_digit(y_coor: int, x_coor: int):

    digit_array = []
    global sum_of_parts

    while schematic_array[y_coor][x_coor - 1].isdigit():
        
        if x_coor - 1 >= 0:
            x_coor = x_coor - 1

    while schematic_array[y_coor][x_coor].isdigit():
        
        digit_array.append(schematic_array[y_coor][x_coor])
        schematic_array[y_coor][x_coor] = '.'
        x_coor = x_coor + 1

        if x_coor > 139:
            break

    digit = int(''.join(digit_array))

    sum_of_parts = sum_of_parts + digit


def check_for_digits_around(y_coor: int, x_coor: int):

    if schematic_array[y_coor - 1][x_coor - 1].isdigit():   #top left

        find_full_digit(y_coor - 1, x_coor - 1)

    if schematic_array[y_coor - 1][x_coor].isdigit():       #top

        find_full_digit(y_coor - 1, x_coor)

    if schematic_array[y_coor - 1][x_coor + 1].isdigit():   #top right

        find_full_digit(y_coor - 1, x_coor + 1)

    if schematic_array[y_coor][x_coor - 1].isdigit():       #left

        find_full_digit(y_coor, x_coor - 1)

    if schematic_array[y_coor][x_coor + 1].isdigit():       #right

        find_full_digit(y_coor, x_coor + 1)

    if schematic_array[y_coor + 1][x_coor - 1].isdigit():   #bottom left

        find_full_digit(y_coor + 1, x_coor - 1)
    
    if schematic_array[y_coor + 1][x_coor].isdigit():       #bottom

        find_full_digit(y_coor + 1, x_coor)

    if schematic_array[y_coor + 1][x_coor + 1].isdigit():   #bottom right

            find_full_digit(y_coor + 1, x_coor + 1)


def check_for_special_characters(schematic_array: list[list]):

    y_coor = 0
    x_coor = 0

    for line in schematic_array:
        for character in line:
            if not character.isdigit() and character != '.':
                check_for_digits_around(y_coor, x_coor)
            
            x_coor = x_coor + 1
        
        x_coor = 0
        y_coor = y_coor + 1

def main():

    with open("_input/input.txt", "r") as file:

        for line in file.readlines():
            line = line.strip('\n')
            line_data = list(line)
            schematic_array.append(line_data)

        #schematic_array[y][x]

    check_for_special_characters(schematic_array)
    
    print(sum_of_parts)



if __name__ == '__main__':
    main()