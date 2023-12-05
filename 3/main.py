#global variables
schematic_array = []

def check_for_digits_around(y_coor: int, x_coor: int):

    print(y_coor, ", ", x_coor)

    if schematic_array[y_coor - 1][x_coor - 1].isdigit():   #top left
        print('digit found')

    if schematic_array[y_coor - 1][x_coor].isdigit():       #top
        print('digit found')

    if schematic_array[y_coor - 1][x_coor + 1].isdigit():   #top right
        print('digit found')
    
    if schematic_array[y_coor][x_coor - 1].isdigit():       #left
        print('digit found')

    if schematic_array[y_coor][x_coor + 1].isdigit():       #right
        print('digit found')
    
    if schematic_array[y_coor + 1][x_coor - 1].isdigit():   #bottom left
        print('digit found')
    
    if schematic_array[y_coor + 1][x_coor].isdigit():       #bottom
        print('digit found')

    if schematic_array[y_coor + 1][x_coor + 1].isdigit():   #bottom right
        print('digit found')


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
    



if __name__ == '__main__':
    main()