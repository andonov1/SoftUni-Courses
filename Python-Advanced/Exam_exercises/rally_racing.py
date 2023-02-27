def get_next_position(position, command):
    if command == 'up':
        return [position[0] - 1, position[1]]
    elif command == 'down':
        return [position[0] + 1, position[1]]
    elif command == 'left':
        return [position[0], position[1] - 1]
    else:
        return [position[0], position[1] + 1]


n = int(input())
racing_number = input()
matrix = []
car_coordinates = [0, 0]
passed_kilometers = 0
tunnels = []

for i in range(n):
    matrix.append([s for s in input().split()])
    for j in range(n):
        if matrix[i][j] == 'T':
            tunnels.append([i, j])

while True:
    command = input()
    if command == "End":
        print(f"Racing car {racing_number} DNF.")
        break
    matrix[car_coordinates[0]][car_coordinates[1]] = '.'
    car_coordinates = get_next_position(car_coordinates, command)

    if matrix[car_coordinates[0]][car_coordinates[1]] == 'T':
        passed_kilometers += 30
        matrix[car_coordinates[0]][car_coordinates[1]] = '.'
        if tunnels[0] != car_coordinates:
            car_coordinates = [tunnels[0][0], tunnels[0][1]]
        else:
            car_coordinates = [tunnels[1][0], tunnels[1][1]]

    elif matrix[car_coordinates[0]][car_coordinates[1]] == 'F':
        passed_kilometers += 10
        print(f"Racing car {racing_number} finished the stage!")
        break
    else:
        passed_kilometers += 10

print(f"Distance covered {passed_kilometers} km.")
matrix[car_coordinates[0]][car_coordinates[1]] = 'C'
for row in matrix:
    print(*row, sep='')
