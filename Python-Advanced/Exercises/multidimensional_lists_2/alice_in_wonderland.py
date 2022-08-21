def is_valid(row, col, matrix):
    return 0 <= row < len(matrix) and 0 <= col < len(matrix)



def get_next_pos(direction, row, col):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


n = int(input())
matrix = []
alice_row = None
alice_col = None
collected_tea = 0

for row in range(n):
    matrix.append([x for x in input().split()])

    for col in range(n):
        if matrix[row][col] == 'A':
            alice_row = row
            alice_col = col

while True:
    direction = input()
    matrix[alice_row][alice_col] = '*'
    alice_row, alice_col = get_next_pos(direction, alice_row, alice_col)
    if is_valid(alice_row, alice_col, matrix):
        if matrix[alice_row][alice_col].isdigit():
            collected_tea += int(matrix[alice_row][alice_col])
        elif matrix[alice_row][alice_col] == 'R':
            matrix[alice_row][alice_col] = '*'
            print("Alice didn't make it to the tea party.")
            break
        else:
            continue
    else:
        print("Alice didn't make it to the tea party.")
        break
    if collected_tea >= 10:
        matrix[alice_row][alice_col] = '*'
        print("She did it! She went to the party.")
        break
for row in matrix:
    print(*row)
