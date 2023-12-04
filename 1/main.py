def turn_words_into_digits(coordinate: str) -> str:

    list_of_words = [['zero', '0'], ['one', '1'], ['two', '2'], ['three', '3'], ['four', '4'], 
                    ['five', '5'], ['six', '6'], ['seven', '7'], ['eight', '8'], ['nine', '9']]

    for word_digit_pair in list_of_words:
        if word_digit_pair[0] in coordinate:
            replace = word_digit_pair[0] + word_digit_pair[1] + word_digit_pair[0]
            coordinate = coordinate.replace(word_digit_pair[0], replace)

    return coordinate

def split_coordinates_to_list(coordinate: str) -> list:

    list_of_characters = list(coordinate)

    return list_of_characters

def find_first_digit(list_of_characters: list) -> int:

    for character in list_of_characters:

        if character.isdigit():
            first_digit = character
            return int(first_digit)
        
def find_last_digit(list_of_characters: list) -> int:

    for character in list_of_characters:

        if character.isdigit():
            last_digit = character
    
    return int(last_digit)

def combine_digits_together(list_of_digits: list) -> list:

    list_of_sums = []
    for digit_pairs in list_of_digits:
        list_of_sums.append(int(''.join(str(num) for num in digit_pairs)))

    return list_of_sums

def elf_coordinate_file_read() -> int:

    with open("_input/input.txt", "r") as file:

        coordinate_str = file.read()
        coordinate_list = coordinate_str.split('\n')

        list_of_digits = []

        for coordinate in coordinate_list:
            print(coordinate)
            replaced_coordinate = turn_words_into_digits(coordinate)
            print(replaced_coordinate)
            list_of_charcters = split_coordinates_to_list(replaced_coordinate)
            first_digit = find_first_digit(list_of_charcters)
            last_digit = find_last_digit(list_of_charcters)
            print(first_digit, ', ', last_digit)

            list_of_digits.append([first_digit, last_digit])

        list_of_sums = combine_digits_together(list_of_digits)

        total = sum(list_of_sums)

        print(total)


if __name__ == '__main__':
    elf_coordinate_file_read()