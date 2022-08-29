rows = int(input())
matrix = [[int(j) for j in input().split(', ')] for i in range(rows)]
primary_diagonal = []
secondary_diagonal = []

for index in range(rows):
    primary_diagonal.append(matrix[index][index])
for index in range(rows):
    secondary_diagonal.append(matrix[index][rows - 1 - index])

print(f"Primary diagonal: {', '.join([str(s) for s in primary_diagonal])}. Sum: {sum(primary_diagonal)}\n"
      f"Secondary diagonal: {', '.join([str(s) for s in secondary_diagonal])}. Sum: {sum(secondary_diagonal)}")
