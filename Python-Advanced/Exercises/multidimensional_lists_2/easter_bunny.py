import sys


def is_valid(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


def move_up(row, col):
    return (row - 1, col)


def move_down(row, col):
    return (row + 1, col)


def move_left(row, col):
    return (row, col - 1)


def move_right(row, col):
    return (row, col + 1)


n = int(input())
matrix = []
bunny_row = None
bunny_col = None
for row in range(n):
    matrix.append([s for s in input().split()])
    for col in range(n):
        if matrix[row][col] == 'B':
            bunny_row, bunny_col = (row, col)

directions = {
    'up': move_up,
    'down': move_down,
    'left': move_left,
    'right': move_right
}
best_path = None
best_direction = None
best_result = -sys.maxsize
for direction, command in directions.items():
    current_path = []
    result = 0
    current_row, current_col = command(bunny_row, bunny_col)
    while True:
        if is_valid(current_row, current_col, matrix) and matrix[current_row][current_col] != 'X':
            result += int(matrix[current_row][current_col])
            current_path.append([current_row, current_col])
        else:
            if result > best_result and current_path:
                best_result = result
                best_direction = direction
                best_path = current_path
            break
        current_row, current_col = command(current_row, current_col)

print(best_direction)
for path in best_path:
    print(path)
print(best_result)
