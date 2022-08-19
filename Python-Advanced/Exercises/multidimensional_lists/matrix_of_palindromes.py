rows, cols = [int(s) for s in input().split()]
matrix = []

for row in range(rows):
    for col in range(cols):
        print(f'{chr(row + 97)}{chr(row + col + 97)}{chr(row + 97)}', end=' ')
    print()
