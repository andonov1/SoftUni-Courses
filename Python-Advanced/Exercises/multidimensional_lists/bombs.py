def is_inside(row, col, size):
    return 0 <= row < size and 0 <= col < size


def get_neighbours(row, col, matrix):
    size = len(matrix)
    neighbours = []
    if is_inside(row - 1, col - 1, size):
        neighbours.append([row - 1, col - 1])
    if is_inside(row - 1, col, size):
        neighbours.append([row - 1, col])
    if is_inside(row - 1, col + 1, size):
        neighbours.append([row - 1, col + 1])
    if is_inside(row, col - 1, size):
        neighbours.append([row, col - 1])
    if is_inside(row, col + 1, size):
        neighbours.append([row, col + 1])
    if is_inside(row + 1, col - 1, size):
        neighbours.append([row + 1, col - 1])
    if is_inside(row + 1, col, size):
        neighbours.append([row + 1, col])
    if is_inside(row + 1, col + 1, size):
        neighbours.append([row + 1, col + 1])
    return neighbours


n = int(input())
matrix = []

for row in range(n):
    matrix.append([int(s) for s in input().split()])

bombs = input().split()
for bomb in bombs:
    bomb_row, bomb_col = [int(s) for s in bomb.split(',')]
    bomb_power = matrix[bomb_row][bomb_col]
    if bomb_power <= 0:
        continue
    neighbours = get_neighbours(bomb_row, bomb_col, matrix)
    for neighbour in neighbours:
        if matrix[neighbour[0]][neighbour[1]] > 0:
            matrix[neighbour[0]][neighbour[1]] -= bomb_power
    matrix[bomb_row][bomb_col] = 0

alive_cells = 0
sum_of_alive_cells = 0

for row in range(n):
    for col in range(n):
        if matrix[row][col] > 0:
            alive_cells += 1
            sum_of_alive_cells += matrix[row][col]

print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_of_alive_cells}")
for row in matrix:
    print(*row)
