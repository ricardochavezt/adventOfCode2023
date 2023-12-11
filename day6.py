import fileinput
import re
import math

line_pattern = re.compile(r'\w+:\s+([\d\s]+)')
lines = list(fileinput.input())

time_digits = line_pattern.match(lines[0])[1].split()
times = [int(t) for t in time_digits]
distance_digits = line_pattern.match(lines[1])[1].split()
distances = [int(d) for d in distance_digits]

def count_ways_to_win(t, d):
    #quadratic equation - thank you Reddit xD
    quad_discriminant = math.sqrt((t ** 2) - 4 * d)
    upper_bound = (t + quad_discriminant) / 2
    lower_bound = (t - quad_discriminant) / 2
    ways_to_win = math.ceil(upper_bound - 1) - math.floor(lower_bound + 1) + 1
    return ways_to_win

final_value = 1
for (t, d) in zip(times, distances):
    ways_to_win = count_ways_to_win(t, d)
    final_value *= ways_to_win

print("Part 1:", final_value)

only_one_time = int(''.join(time_digits))
onyl_one_distance = int(''.join(distance_digits))

print("Part 2:", count_ways_to_win(only_one_time, onyl_one_distance))