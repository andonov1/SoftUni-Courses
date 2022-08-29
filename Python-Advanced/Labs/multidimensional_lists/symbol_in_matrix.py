square_matrix = int(input())
matrix = []
searched_char_position = None

for _ in range(square_matrix):
    matrix.append(list(input()))

searched_char = input()

for row in range(square_matrix):
    for col in range(square_matrix):
        if searched_char == matrix[row][col]:
            searched_char_position = (row, col)
            break
    if searched_char_position:
        break

if searched_char_position:
    print(searched_char_position)
else:
    print(f"{searched_char} does not occur in the matrix")