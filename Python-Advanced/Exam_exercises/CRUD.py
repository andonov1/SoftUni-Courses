def get_next_position(position, direction):
    if direction == 'up':
        return position[0] - 1, position[1]
    elif direction == 'down':
        return position[0] + 1, position[1]
    elif direction == 'left':
        return position[0], position[1] - 1
    elif direction == 'right':
        return position[0], position[1] + 1


matrix = []

for i in range(6):
    matrix.append(input().split())

data = input().split(', ')
current_position = (int(data[0][1]), int(data[1][0]))

while True:
    command = input()
    if command == 'Stop':
        break
    command = command.split(', ')
    action = command[0]
    direction = command[1]

    current_position = get_next_position(current_position, direction)
    if action == 'Create':
        if matrix[current_position[0]][current_position[1]] == '.':
            matrix[current_position[0]][current_position[1]] = command[2]
    elif action == 'Update':
        if matrix[current_position[0]][current_position[1]] != '.':
            matrix[current_position[0]][current_position[1]] = command[2]
    elif action == 'Delete':
        if matrix[current_position[0]][current_position[1]] != '.':
            matrix[current_position[0]][current_position[1]] = '.'
    else:
        if matrix[current_position[0]][current_position[1]] != '.':
            print(matrix[current_position[0]][current_position[1]])

for row in matrix:
    print(*row)