rows = int(input())

flattened_matrix = []

for _ in range(rows):
    line = [int(s) for s in input().split(', ')]
    flattened_matrix.extend(line)

print(flattened_matrix)