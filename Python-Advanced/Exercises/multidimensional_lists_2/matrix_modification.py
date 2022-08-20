def is_valid(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)


n = int(input())
matrix = []

for row in range(n):
    matrix.append([int(s) for s in input().split()])

while True:
    command = input().split()
    if command[0] == 'END':
        break
    action = command[0]
    row, col, value = [int(s) for s in command[1:]]
    if is_valid(row, col, matrix):
        if action == 'Add':
            matrix[row][col] += value
        else:
            matrix[row][col] -= value
    else:
        print('Invalid coordinates')
for row in matrix:
    print(*row)