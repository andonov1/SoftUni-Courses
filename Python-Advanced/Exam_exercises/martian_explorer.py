def get_next_position(position, direction):
    if direction == 'up':
        if position[0] - 1 < 0:
            return 5, position[1]
        return position[0] - 1, position[1]

    elif direction == 'down':
        if position[0] + 1 == 6:
            return 0, position[1]
        return position[0] + 1, position[1]

    elif direction == 'left':
        if position[1] - 1 < 0:
            return position[0], 5
        return position[0], position[1] - 1

    elif direction == 'right':
        if position[1] + 1 == 6:
            return position[0], 0
        return position[0], position[1] + 1


rover_position = None
matrix = []
water = False
metal = False
concrete = False

for row in range(6):
    matrix.append([s for s in input().split()])
    for col in range(6):
        if matrix[row][col] == 'E':
            rover_position = (row, col)

commands = input().split(', ')

for command in commands:
    next_position = get_next_position(rover_position, command)
    item = matrix[next_position[0]][next_position[1]]

    if item == 'R':
        print(f"Rover got broken at ({next_position[0]}, {next_position[1]})")
        break

    elif item == 'W':
        water = True
        print(f"Water deposit found at ({next_position[0]}, {next_position[1]})")
    elif item == 'M':
        print(f"Metal deposit found at ({next_position[0]}, {next_position[1]})")
        metal = True
    elif item == 'C':
        print(f"Concrete deposit found at ({next_position[0]}, {next_position[1]})")
        concrete = True
    rover_position = next_position

if water and metal and concrete:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
