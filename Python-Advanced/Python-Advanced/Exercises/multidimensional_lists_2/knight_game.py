def is_valid(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


def collisions(row, col):
    current_collisions = 0
    if is_valid(row - 2, col - 1, matrix) and matrix[row - 2][col - 1] == 'K':
        current_collisions += 1
    if is_valid(row - 2, col + 1, matrix) and matrix[row - 2][col + 1] == 'K':
        current_collisions += 1
    if is_valid(row - 1, col - 2, matrix) and matrix[row - 1][col - 2] == 'K':
        current_collisions += 1
    if is_valid(row - 1, col + 2, matrix) and matrix[row - 1][col + 2] == 'K':
        current_collisions += 1
    if is_valid(row + 1, col - 2, matrix) and matrix[row + 1][col - 2] == 'K':
        current_collisions += 1
    if is_valid(row + 1, col + 2, matrix) and matrix[row + 1][col + 2] == 'K':
        current_collisions += 1
    if is_valid(row + 2, col - 1, matrix) and matrix[row + 2][col - 1] == 'K':
        current_collisions += 1
    if is_valid(row + 2, col + 1, matrix) and matrix[row + 2][col + 1] == 'K':
        current_collisions += 1
    return current_collisions


n = int(input())
matrix = []
removed_knights = 0
for row in range(n):
    matrix.append([s for s in input()])

while True:
    max_collisions = 0
    max_collisions_knight = None
    knight_collisions = {}
    for row in range(n):
        for col in range(n):
            if matrix[row][col] == 'K':
                if collisions(row, col):
                    knight_collisions[(row, col)] = collisions(row, col)
    if not knight_collisions:
        break
    for knight, collision_value in knight_collisions.items():
        if collision_value > max_collisions:
            max_collisions = collision_value
            max_collisions_knight = knight
    row, col = max_collisions_knight
    matrix[row][col] = '0'
    removed_knights += 1
print(removed_knights)
