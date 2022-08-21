def get_next_pos(direction, row, col):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


presents = int(input())
size = int(input())
matrix = []
santa_row = None
santa_col = None
nice_kids = 0
delivered_presents_to_good_kids = 0

for row in range(size):
    matrix.append([s for s in input().split()])
    for col in range(size):
        if matrix[row][col] == 'S':
            santa_row = row
            santa_col = col
        if matrix[row][col] == 'V':
            nice_kids += 1

while True:
    command = input()
    if command == 'Christmas morning':
        break
    matrix[santa_row][santa_col] = '-'
    santa_row, santa_col = get_next_pos(command, santa_row, santa_col)
    if matrix[santa_row][santa_col] == 'V':
        delivered_presents_to_good_kids += 1
        presents -= 1
    elif matrix[santa_row][santa_col] == 'C':
        if matrix[santa_row][santa_col - 1] == 'V' and presents:
            delivered_presents_to_good_kids += 1
            presents -= 1
            matrix[santa_row][santa_col - 1] = '-'
        elif matrix[santa_row][santa_col - 1] == 'X' and presents:
            presents -= 1
            matrix[santa_row][santa_col - 1] = '-'
        if matrix[santa_row][santa_col + 1] == 'V' and presents:
            delivered_presents_to_good_kids += 1
            presents -= 1
            matrix[santa_row][santa_col + 1] = '-'
        elif matrix[santa_row][santa_col + 1] == 'X' and presents:
            presents -= 1
            matrix[santa_row][santa_col + 1] = '-'
        if matrix[santa_row - 1][santa_col] == 'V' and presents:
            delivered_presents_to_good_kids += 1
            presents -= 1
            matrix[santa_row - 1][santa_col] = '-'
        elif matrix[santa_row - 1][santa_col] == 'X' and presents:
            presents -= 1
            matrix[santa_row - 1][santa_col] = '-'
        if matrix[santa_row + 1][santa_col] == 'V' and presents:
            delivered_presents_to_good_kids += 1
            presents -= 1
            matrix[santa_row + 1][santa_col] = '-'
        elif matrix[santa_row + 1][santa_col] == 'X' and presents:
            presents -= 1
            matrix[santa_row + 1][santa_col] = '-'

    matrix[santa_row][santa_col] = 'S'
    if presents == 0:
        break
if presents == 0 and delivered_presents_to_good_kids < nice_kids:
    print("Santa ran out of presents!")
for row in matrix:
    print(*row, sep=' ')
if nice_kids == delivered_presents_to_good_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids - delivered_presents_to_good_kids} nice kid/s.")




