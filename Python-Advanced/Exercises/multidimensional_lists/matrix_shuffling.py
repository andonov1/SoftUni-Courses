def is_outside(row1, col1, rows, cols):
    return row1 < 0 or col1 < 0 or row1 > rows or col1 > cols


rows, cols = [int(s) for s in input().split()]
matrix = []

for j in range(rows):
    matrix.append([int(s) for s in input().split()])

command = input()

while command != 'END':
    command = command.split()
    if len(command) != 5 or command[0] != 'swap':
        print('Invalid input!')
        command = input()
        continue
    row1, col1, row2, col2 = [int(s) for s in command[1:]]

    if is_outside(row1, col1, rows, cols) or is_outside(row2, col2, rows, cols):
        print('Invalid input!')
        command = input()
        continue
    else:
        matrix[row1][col1], matrix[row2][col2] = matrix[row2][col2], matrix[row1][col1]
        for row in range(rows):
            print(*matrix[row])
        command = input()
