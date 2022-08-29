rows, cols = [int(s) for s in input().split(', ')]
max_submatrix_sum = -999999999999999
matrix = []
max_submatrix = []

for _ in range(rows):
    matrix.append([int(s) for s in input().split(', ')])

for row in range(rows - 1):
    for col in range(cols - 1):
        current_submatrix = [matrix[row][col], matrix[row][col + 1], matrix[row + 1][col], matrix[row + 1][col + 1]]
        if sum(current_submatrix) > max_submatrix_sum:
            max_submatrix_sum = sum(current_submatrix)
            max_submatrix= current_submatrix.copy()

print(f'{max_submatrix[0]} {max_submatrix[1]}')
print(f'{max_submatrix[2]} {max_submatrix[3]}')
print(max_submatrix_sum)
