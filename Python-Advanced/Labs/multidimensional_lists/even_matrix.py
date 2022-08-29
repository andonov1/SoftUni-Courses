rows = int(input())

matrix = [[int(s) for s in input().split(', ') if int(s) % 2 == 0] for _ in range(rows)]
print(matrix)