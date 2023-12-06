import fileinput
import re

def convert_digit(alphanum):
    match alphanum:
        case "one":
            return 1
        case "two":
            return 2
        case "three":
            return 3
        case "four":
            return 4
        case "five":
            return 5
        case "six":
            return 6
        case "seven":
            return 7
        case "eight":
            return 8
        case "nine":
            return 9
        case _:
            return int(alphanum)

pattern = r'\d'
pattern2 = r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))' # positive lookahead to get overlapping numbers
sum = 0
sum_part_2 = 0
for line in fileinput.input():
    digits = re.findall(pattern, line[:-1])
    if len(digits) > 0:
        value = int(digits[0]) * 10 + int(digits[-1])
        sum += value

    digits_part_2 = re.findall(pattern2, line[:-1])
    if len(digits_part_2) > 0:
        value_part_2 = convert_digit(digits_part_2[0]) * 10 + convert_digit(digits_part_2[-1])
        sum_part_2 += value_part_2

print("Part 1:", sum)
print("Part 2:", sum_part_2)