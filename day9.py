import fileinput

sequences = []
for line in fileinput.input():
    initial_sequence = [int(i) for i in line.strip().split()]
    current_sequence = initial_sequence
    all_equal = False
    differences_stack = []
    while not all_equal:
        current_differences = []
        for i in range(1, len(current_sequence)):
            current_differences.append(current_sequence[i] - current_sequence[i-1])
            if len(current_differences) > 1:
                all_equal = (current_differences[-1] == current_differences[-2])

        # print(current_differences)
        differences_stack.append(current_differences)
        current_sequence = current_differences
    
    # print('--')
    while len(differences_stack) > 0:
        current_differences = differences_stack.pop()
        next_sequence = differences_stack[-1] if len(differences_stack) > 0 else initial_sequence
        next_sequence.append(next_sequence[-1] + current_differences[-1])
        next_sequence.insert(0, next_sequence[0] - current_differences[0])

    sequences.append(initial_sequence)
    # print(initial_sequence)
    # print('---')

print('Part 1:', sum([s[-1] for s in sequences]))
print('Part 2:', sum([s[0] for s in sequences]))