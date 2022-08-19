rows, cols = [int(s) for s in input().split()]
matrix = [[int(j) for j in input().split()] for i in range(rows)]
max_sum_squares = []
max_sum = -999999999999

for row in range(rows - 2):
    for col in range(cols - 2):
        current_square = [matrix[row][col], matrix[row][col + 1], matrix[row][col + 2],
                          matrix[row + 1][col], matrix[row + 1][col + 1], matrix[row + 1][col + 2],
                          matrix[row + 2][col], matrix[row + 2][col + 1], matrix[row + 2][col + 2]]
        if sum(current_square) > max_sum:
            max_sum = sum(current_square)
            max_sum_squares = []
            max_sum_squares.extend(current_square)

print(f'Sum = {max_sum}')
counter = 0
for i in range(len(max_sum_squares)):
    counter += 1
    print(max_sum_squares[i], end=' ')
    if counter == 3:
        counter = 0
        print()