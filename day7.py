import fileinput
import re

line_pattern = re.compile(r'(\w+)\s+(\d+)')
hands = []

def sorted_hand(hand, with_joker=False):
    sorted_cards = sorted(hand)
    last_card = ''
    grouped_cards = []
    for c in sorted_cards:
        if last_card != c:
            grouped_cards.append([])
        grouped_cards[-1].append(c)
        last_card = c
    
    result = [''.join(g) for g in grouped_cards]
    result.sort(key=lambda r: len(r), reverse=True)
    if with_joker and len(result) > 1:
        joker_group_index = -1
        for (i, g) in enumerate(result):
            if g[0] == 'J':
                joker_group_index = i
                break
        if joker_group_index != -1:
            joker_group = result.pop(joker_group_index)
            result[0] += joker_group

    return result

sorted_cards = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
sorted_cards_joker = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']
def hand_sort_rank(hand, with_joker=False):
    rank_1st = 7
    match sorted_hand(hand, with_joker):
        case [c] if len(c) == 5:
            rank_1st = 0
        case [c1, c2] if len(c1) == 4:
            rank_1st = 1
        case [c1, c2] if len(c1) == 3:
            rank_1st = 2
        case [c1, c2, c3] if len(c1) == 3:
            rank_1st = 3
        case [c1, c2, c3] if len(c1) == 2 and len(c2) == 2:
            rank_1st = 4
        case [c1, c2, c3, c4] if len(c1) == 2:
            rank_1st = 5
        case _:
            rank_1st = 6

    rank_2nd = 0
    base = len(sorted_cards_joker) if with_joker else len(sorted_cards)
    for card in hand:
        rank_2nd *= base
        try:
            rank_2nd += (sorted_cards_joker.index(card) if with_joker else sorted_cards.index(card))
        except:
            rank_2nd += base

    return (rank_1st, rank_2nd)

for line in fileinput.input():
    line_match = line_pattern.match(line.strip())
    hand = (line_match[1], int(line_match[2]))
    hands.append(hand)

hands_sorted = sorted(hands, key=lambda h: hand_sort_rank(h[0]), reverse=True)
# print(hands_sorted)
print("Part 1:", sum([(rank+1) * h[1] for (rank, h) in enumerate(hands_sorted)]))
hands_sorted_jokers = sorted(hands, key=lambda h: hand_sort_rank(h[0], with_joker=True), reverse=True)
# print(hands_sorted_jokers)
print("Part 2:", sum([(rank+1) * h[1] for (rank, h) in enumerate(hands_sorted_jokers)]))