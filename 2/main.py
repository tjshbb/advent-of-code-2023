def split_game(game: str) -> tuple:

    game_number = int(game.split(':')[0])
    game_attempts = game.split(':')[1]

    return game_number, game_attempts

def find_max_for_color(game_attempts: str) -> tuple:

    blue_max = 0
    green_max = 0
    red_max = 0

    games = game_attempts.split(';')

    for game in games:
        
        hand = (game.split(','))

        for color_number in hand:

            number = int(color_number.split(' ')[1])
            color = color_number.split(' ')[2]

            if color == 'red' and number > red_max:
                red_max = number
            
            if color == 'green' and number > green_max:
                green_max = number

            if color == 'blue' and number > blue_max:
                blue_max = number

    return red_max, green_max, blue_max

def find_number_of_cubes(r_max: int, g_max: int, b_max: int) -> int:

    return r_max*g_max*b_max

def is_valid_game(r_max: int, g_max: int, b_max: int) -> bool:

    if r_max > 12:
        return False

    if g_max > 13:
        return False

    if b_max > 14:
        return False
    
    return True


def game_admin():

    sum_of_games = 0
    sum_of_cubes = 0

    with open("_input/input.txt", "r") as file:

        game_str = file.read()

    game_str = game_str.replace('Game', '')

    list_of_games = game_str.split('\n')

    for game in list_of_games:
        game_number, game_attempts = split_game(game)
        r_max, g_max, b_max = find_max_for_color(game_attempts)
        number_of_cubes = find_number_of_cubes(r_max, g_max, b_max)
        valid_game = is_valid_game(r_max, g_max, b_max)

        if valid_game:
            sum_of_games = sum_of_games + game_number

        sum_of_cubes = sum_of_cubes + number_of_cubes

    print(sum_of_games)
    print(sum_of_cubes)


if __name__ == '__main__':
    game_admin()