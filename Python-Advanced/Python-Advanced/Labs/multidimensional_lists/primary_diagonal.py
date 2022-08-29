size_square = int(input())
matrix = []

for _ in range(size_square):
    line = [int(s) for s in input().split()]
    matrix.append(line)

diagonal_sum = 0
for i in range(size_square):
    diagonal_sum += matrix[i][i]

print(diagonal_sum)