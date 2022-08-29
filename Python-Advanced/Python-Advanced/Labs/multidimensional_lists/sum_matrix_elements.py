rows, cols = [int(s) for s in input().split(', ')]
matrix = []
total_sum = 0

for row in range(rows):
    lines = [int(s) for s in input().split(', ')]
    total_sum += sum(lines)
    matrix.append(lines)

print(total_sum)
print(matrix)