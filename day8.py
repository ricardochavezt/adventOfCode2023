import fileinput
import re
from functools import reduce

instructions_pattern = re.compile(r'([RL]+)')
network_line_pattern = re.compile(r'(\w+)\s+=\s+\((\w+),\s+(\w+)\)')

def follow_path(starting_node, end_mode):
    current_node = starting_node
    instructions_index, instructions_counter = 0, 0
    end_reached = False
    while not end_reached:
        direction = instructions[instructions_index]
        left_node, right_node = network[current_node]
        current_node = left_node if direction == 'L' else right_node
        instructions_index += 1
        if instructions_index >= len(instructions):
            instructions_index = 0
        instructions_counter += 1
        end_reached = (current_node == 'ZZZ') if end_mode == 1 else (current_node[-1] == 'Z')
    
    return instructions_counter

def lcm(a, b):
    return a // gcd(a, b) * b

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

instructions = ''
network = dict()
starting_nodes = []
for line in fileinput.input():
    if (instructions_match := instructions_pattern.fullmatch(line.strip())):
        instructions = instructions_match[1]
    elif (network_line_match := network_line_pattern.match(line.strip())):
        network[network_line_match[1]] = network_line_match.group(2, 3)
        if network_line_match[1][-1] == 'A':
            starting_nodes.append(network_line_match[1])

if 'AAA' in network:
    instructions_counter = follow_path('AAA', 1)
    print("Part 1:", instructions_counter)

instructions_count_list = []
for start_node in starting_nodes:
    instructions_count_list.append(follow_path(start_node, 2))

lcm_all = reduce(lcm, instructions_count_list)
print("Part 2:", lcm_all)