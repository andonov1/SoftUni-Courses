rows = int(input())
matrix = [[int(j) for j in input().split()] for i in range(rows)]
primary_diagonal = []
secondary_diagonal = []

for index in range(rows):
    primary_diagonal.append(matrix[index][index])
for index in range(rows):
    secondary_diagonal.append(matrix[index][rows - 1 - index])

print(abs(sum(primary_diagonal)-sum(secondary_diagonal)))
