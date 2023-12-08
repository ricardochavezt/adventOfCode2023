import fileinput
import re

whole_line_pattern = re.compile(r'Game (\d+): (.*)')
cube_pattern = re.compile(r'(\d+) (red|blue|green)')

sum_game_ids = 0
sum_powers = 0
for line in fileinput.input():
    print(line[:-1])
    game_id, sets = whole_line_pattern.match(line).group(1, 2)
    is_game_possible = True
    min_required_green, min_required_red, min_required_blue = 0, 0, 0
    for set in sets.split(';'):
        print(set)
        possible_green, possible_red, possible_blue = True, True, True
        for cube in set.split(','):
            str_number, color = cube_pattern.match(cube.strip()).group(1, 2)
            number_cubes = int(str_number)
            match color:
                case 'green':
                    possible_green = number_cubes <= 13
                    min_required_green = number_cubes if number_cubes > min_required_green else min_required_green
                case 'blue':
                    possible_blue = number_cubes <= 14
                    min_required_blue = number_cubes if number_cubes > min_required_blue else min_required_blue
                case 'red':
                    possible_red = number_cubes <= 12
                    min_required_red = number_cubes if number_cubes > min_required_red else min_required_red
                case _:
                    pass
        print('possible_blue:', possible_blue, 'possible_green:', possible_green, 'possible_red:', possible_red)
        is_game_possible = is_game_possible and (possible_blue and possible_green and possible_red)
    if is_game_possible:
        sum_game_ids += int(game_id)
    sum_powers += (min_required_blue * min_required_green * min_required_red)

print('Part 1:', sum_game_ids)
print('Part 2:', sum_powers)