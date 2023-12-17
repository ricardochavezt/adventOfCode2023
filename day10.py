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
while map[next_row][next_col] != "S":
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
            if direction == Direction.LEFT:
                direction = Direction.UP
                next_row -= 1
            else:
                direction = Direction.RIGHT
                next_col += 1
        case "J":
            if direction == Direction.DOWN:
                direction = Direction.LEFT
                next_col -= 1
            else:
                direction = Direction.UP
                next_row -= 1
        case "7":
            if direction == Direction.RIGHT:
                direction = Direction.DOWN
                next_row += 1
            else:
                direction = Direction.LEFT
                next_col -= 1
        case "F":
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