import fileinput
from enum import Enum

class Direction(Enum):
    UP = 1
    DOWN = 2
    LEFT = 3
    RIGHT = 4

map = list(fileinput.input())
# find starting point
starting_row, starting_col = 0, 0
for (row, l) in enumerate(map):
    col = l.find('S')
    if col != -1:
        starting_row, starting_col = row, col
        break

# find connecting pipes from start
next_row, next_col = 0, 0
direction = None
if starting_row > 0 and map[starting_row-1][starting_col] in "|7F":
    next_row, next_col = starting_row - 1, starting_col
    direction = Direction.UP
elif starting_col < len(map[starting_row])-1 and map[starting_row][starting_col+1] in "-7J":
    next_row, next_col = starting_row, starting_col + 1
    direction = Direction.RIGHT
elif starting_row < len(map)-1 and map[starting_row+1][starting_col] in "|LJ":
    next_row, next_col = starting_row + 1, starting_col
    direction = Direction.DOWN
elif starting_col > 0 and map[starting_row][starting_col-1] in "-LF":
    next_row, next_col = starting_row, starting_col - 1
    direction = Direction.LEFT

# follow the path
path_counter = 1
connecting_from_start_row, connecting_from_start_col = next_row, next_col
connecting_from_start_row_2, connecting_from_start_col_2 = 0, 0
vertices = []
while map[next_row][next_col] != "S":
    connecting_from_start_row_2, connecting_from_start_col_2 = next_row, next_col
    match map[next_row][next_col]:
        case "|":
            if direction == Direction.UP:
                next_row -= 1
            else:
                next_row += 1
        case "-":
            if direction == Direction.RIGHT:
                next_col += 1
            else:
                next_col -= 1
        case "L":
            vertices.append((next_row, next_col))
            if direction == Direction.LEFT:
                direction = Direction.UP
                next_row -= 1
            else:
                direction = Direction.RIGHT
                next_col += 1
        case "J":
            vertices.append((next_row, next_col))
            if direction == Direction.DOWN:
                direction = Direction.LEFT
                next_col -= 1
            else:
                direction = Direction.UP
                next_row -= 1
        case "7":
            vertices.append((next_row, next_col))
            if direction == Direction.RIGHT:
                direction = Direction.DOWN
                next_row += 1
            else:
                direction = Direction.LEFT
                next_col -= 1
        case "F":
            vertices.append((next_row, next_col))
            if direction == Direction.UP:
                direction = Direction.RIGHT
                next_col += 1
            else:
                direction = Direction.DOWN
                next_row += 1
        case _:
            pass
    path_counter += 1

print("Part 1:", path_counter // 2)

# is the start a corner / vertex?
if not (connecting_from_start_row == connecting_from_start_row_2) and not (connecting_from_start_col == connecting_from_start_col_2):
    vertices.insert(0, (starting_row, starting_col))

# shoelace formula (thank you Reddit xD)
area = 0
for i in range(0, len(vertices)):
    y_i_plus_1, _ = vertices[i+1] if i < len(vertices)-1 else vertices[0]
    area += (vertices[i][1] * (y_i_plus_1 - vertices[i-1][0]))

area = abs(area // 2)

# Pick's theorem (thanks again Reddit xD)
# area = inside_points + (path_counter /// 2) - 1
inside_points = area - (path_counter // 2) + 1

print("Part 2: ", inside_points)