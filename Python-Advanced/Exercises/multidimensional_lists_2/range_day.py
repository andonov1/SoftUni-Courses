def is_valid(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


def get_next_pos(direction, row, col, steps):
    if direction == 'up':
        return row - steps, col
    if direction == 'down':
        return row + steps, col
    if direction == 'left':
        return row, col - steps
    if direction == 'right':
        return row, col + steps


size = 5
matrix = []
player_row = None
player_col = None
targets = 0
targets_hit = 0
targets_hit_positions = []
for row in range(size):
    matrix.append([s for s in input().split()])
    for col in range(size):
        if matrix[row][col] == 'A':
            player_row = row
            player_col = col
        if matrix[row][col] == 'x':
            targets += 1
n = int(input())
for _ in range(n):
    command = input().split()
    action = command[0]
    direction = command[1]
    if action == 'move':
        steps = int(command[2])
        next_row, next_col = get_next_pos(direction, player_row, player_col, steps)
        if is_valid(next_row, next_col, matrix) and matrix[next_row][next_col] == '.':
            matrix[player_row][player_col] = '.'
            player_row, player_col = next_row, next_col
            matrix[player_row][player_col] = 'A'
    else:
        current_row, current_col = player_row, player_col
        while True:
            current_row, current_col = get_next_pos(direction, current_row, current_col, 1)
            if is_valid(current_row, current_col, matrix):
                if matrix[current_row][current_col] == 'x':
                    targets_hit += 1
                    targets_hit_positions.append([current_row, current_col])
                    matrix[current_row][current_col] = '.'
                    break
            else:
                break
    if targets - targets_hit == 0:
        print(f"Training completed! All {targets} targets hit.")
        break

if targets - targets_hit > 0:
    print(f"Training not completed! {targets - targets_hit} targets left.")
for position in targets_hit_positions:
    print(position)
