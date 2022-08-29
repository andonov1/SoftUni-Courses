rows, cols = [int(s) for s in input().split()]
matrix = [[j for j in input().split()] for i in range(rows)]
square_matrices = 0

for row in range(rows-1):
    for col in range(cols-1):
        if matrix[row][col] == matrix[row][col+1] == matrix[row+1][col] == matrix[row+1][col+1]:
            square_matrices += 1

print(square_matrices)

