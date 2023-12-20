import sys
import fileinput

script_options = sys.argv[1:]
part = 1
if len(script_options) > 0:
    part = int(script_options[0])

if part == 1:
    EXPANSION_FACTOR = 2
else:
    EXPANSION_FACTOR = 1000000

if len(script_options) > 1:
    with open(script_options[1], encoding='utf-8') as f:
        lines = [l.strip() for l in list(f)]
else:
    lines = [l.strip() for l in list(sys.stdin)]

current_row = 0
galaxy_positions = []
min_col, max_col = len(lines[0]), 0
for (row, line) in enumerate(lines):
    found_galaxy = False
    for (col, char) in enumerate(line):
        if char == '#':
            found_galaxy = True
            galaxy_positions.append((current_row, col))
            if col < min_col:
                min_col = col
            if col > max_col:
                max_col = col

    # we expand the universe vertically as we go
    # (we duplicate rows if we can't find any galaxies)
    if found_galaxy:
        current_row += 1
    else:
        current_row += EXPANSION_FACTOR

# column expansion
galaxy_positions.sort(key=lambda g: g[1])
previous_col = galaxy_positions[0][1]
expanded = [galaxy_positions[0]]
for i in range(1, len(galaxy_positions)):
    row, col = galaxy_positions[i]
    prev_difference = col - previous_col
    if prev_difference > 1:
        prev_difference = (prev_difference-1) * EXPANSION_FACTOR + 1
    previous_col = col
    expanded.append((row, expanded[i-1][1] + prev_difference))

distance = 0
for (i, g) in enumerate(expanded):
    for j in range(i+1, len(expanded)):
        distance += abs(g[0] - expanded[j][0]) + abs(g[1] - expanded[j][1])

print(f"Part {part}:", distance)