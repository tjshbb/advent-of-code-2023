#global variables
schematic_array = []
sum_of_parts = 0

def find_full_digit(y_coor: int, x_coor: int) -> int:

    digit_array = []

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

    return digit


def check_for_digits_around(y_coor: int, x_coor: int):

    cardinailty_of_point = 0
    global sum_of_parts
    mult_of_point = 1

    if schematic_array[y_coor - 1][x_coor - 1].isdigit():   #top left

        digit = find_full_digit(y_coor - 1, x_coor - 1)
        mult_of_point = mult_of_point * digit

        cardinailty_of_point = cardinailty_of_point + 1

    if schematic_array[y_coor - 1][x_coor].isdigit():       #top

        digit = find_full_digit(y_coor - 1, x_coor)
        mult_of_point = mult_of_point * digit
        
        cardinailty_of_point = cardinailty_of_point + 1

    if schematic_array[y_coor - 1][x_coor + 1].isdigit():   #top right

        digit = find_full_digit(y_coor - 1, x_coor + 1)
        mult_of_point = mult_of_point * digit
        
        cardinailty_of_point = cardinailty_of_point + 1

    if schematic_array[y_coor][x_coor - 1].isdigit():       #left

        digit = find_full_digit(y_coor, x_coor - 1)
        digit = mult_of_point = mult_of_point * digit
        
        cardinailty_of_point = cardinailty_of_point + 1

    if schematic_array[y_coor][x_coor + 1].isdigit():       #right

        digit = find_full_digit(y_coor, x_coor + 1)
        mult_of_point = mult_of_point * digit
        
        cardinailty_of_point = cardinailty_of_point + 1

    if schematic_array[y_coor + 1][x_coor - 1].isdigit():   #bottom left

        digit = find_full_digit(y_coor + 1, x_coor - 1)
        mult_of_point = mult_of_point * digit
        
        cardinailty_of_point = cardinailty_of_point + 1
    
    if schematic_array[y_coor + 1][x_coor].isdigit():       #bottom

        digit = find_full_digit(y_coor + 1, x_coor)
        mult_of_point = mult_of_point * digit
        
        cardinailty_of_point = cardinailty_of_point + 1

    if schematic_array[y_coor + 1][x_coor + 1].isdigit():   #bottom right

        digit = find_full_digit(y_coor + 1, x_coor + 1)
        mult_of_point = mult_of_point * digit
        
        cardinailty_of_point = cardinailty_of_point + 1

    if cardinailty_of_point > 1:
        sum_of_parts = sum_of_parts + mult_of_point


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