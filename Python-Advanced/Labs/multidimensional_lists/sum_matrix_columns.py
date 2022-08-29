rows, cols = [int(s) for s in input().split(', ')]
matrix = []

for row in range(rows):
    line = [int(s) for s in input().split()]
    matrix.append(line)

for col in range(cols):
    current_sum = 0
    for row in range(rows):
        current_sum += matrix[row][col]
    print(current_sum)




