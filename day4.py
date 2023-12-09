import fileinput
import re

line_pattern = re.compile(r'Card\s+(\d+):(.+)\|(.+)')
total_points = 0
copies = dict()

for line in fileinput.input():
    winning_number_count = 0
    line_match = line_pattern.match(line.strip())
    card_number = int(line_match[1])
    copies[card_number] = copies.get(card_number, 0) + 1
    winning_numbers = [int(x) for x in line_match[2].strip().split()]
    my_numbers = [int(x) for x in line_match[3].strip().split()]
    for n in my_numbers:
        if n in winning_numbers:
            winning_number_count += 1
    
    if winning_number_count > 0:
        total_points += (2 ** (winning_number_count-1))
        current_card_copies = copies[card_number]
        for i in range(winning_number_count):
            copies[card_number + 1 + i] = copies.get(card_number + 1 + i, 0) + current_card_copies

print("Part 1:", total_points)
total_cards = 0
for num_copies in copies.values():
    total_cards += num_copies

print("Part 2:", total_cards)