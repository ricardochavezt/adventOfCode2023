import fileinput
import re

part_number_pattern = re.compile(r'\d+')
symbol_pattern = re.compile(r'[^0-9.]')
lines = [l.strip() for l in list(fileinput.input())]
gear_adjacent_parts = dict()

part_number_sum = 0

for index, line in enumerate(lines):
    for m in part_number_pattern.finditer(line):
        part_number = int(m.group())
        # print('Found part number:', part_number, '-', m)
        if m.start() == 0:
            # print('Leftmost side, no symbols to the left')
            check_left = False
        else:
            # print('left string:', line[m.start() - 1])
            check_left = line[m.start() - 1] != '.'
            if line[m.start() - 1] == '*':
                parts = gear_adjacent_parts.get((m.start()-1,index), [])
                parts.append(part_number)
                gear_adjacent_parts[(m.start()-1,index)] = parts

        if m.end() == len(line):
            # print('Rightmost side, no symbols to the right')
            check_right == False
        else:
            # print('right string:', line[m.end()])
            check_right = line[m.end()] != '.'
            if line[m.end()] == '*':
                parts = gear_adjacent_parts.get((m.end(), index), [])
                parts.append(part_number)
                gear_adjacent_parts[(m.end(), index)] = parts

        start_index = m.start() - 1 if m.start() > 0 else 0
        end_index = m.end() + 1 if m.end() < len(line) - 1 else len(line)
        if index == 0:
            check_up = False
        else:
            string_up = lines[index-1][start_index:end_index]
            # print('string_up:', string_up)
            check_up = list(symbol_pattern.finditer(string_up))
            for symbol_match in check_up:
                if symbol_match.group() == '*':
                    parts = gear_adjacent_parts.get((start_index+symbol_match.start(), index-1), [])
                    parts.append(part_number)
                    gear_adjacent_parts[start_index+symbol_match.start(), index-1] = parts
        
        if index == len(lines)-1:
            check_down = False
        else:
            string_down = lines[index+1][start_index:end_index]
            # print('string_down:', string_down)
            check_down = list(symbol_pattern.finditer(string_down))
            for symbol_match in check_down:
                if symbol_match.group() == '*':
                    parts = gear_adjacent_parts.get((start_index+symbol_match.start(), index+1), [])
                    parts.append(part_number)
                    gear_adjacent_parts[start_index+symbol_match.start(), index+1] = parts

        if check_left or check_right or check_up or check_down:
            # print('Part', part_number, 'matches')
            part_number_sum += part_number
        # else:
            # print('Part', part_number, 'does not match')

print('Part 1:', part_number_sum)

gear_ratio_sum = 0
# print('gear_adjacent_parts:', gear_adjacent_parts)
for parts in gear_adjacent_parts.values():
    if len(parts) == 2:
        # print("Found gear between parts", parts[0], "and", parts[1])
        gear_ratio_sum += (parts[0] * parts[1])

print('Part 2:', gear_ratio_sum)