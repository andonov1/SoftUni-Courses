def get_next_position(sub_position, direction):
    if command == 'up':
        return [sub_position[0] - 1, sub_position[1]]
    elif command == 'down':
        return [sub_position[0] + 1, sub_position[1]]
    elif command == 'left':
        return [sub_position[0], sub_position[1] - 1]
    else:
        return [sub_position[0], sub_position[1] + 1]


n = int(input())
matrix = []
submarine_position = None
submarine_health = 2
destroyed_cruisers = 0

for i in range(n):
    matrix.append([s for s in input()])
    for j in range(n):
        if matrix[i][j] == 'S':
            submarine_position = [i, j]

while True:
    command = input()
    matrix[submarine_position[0]][submarine_position[1]] = '-'

    submarine_position = get_next_position(submarine_position, command)

    if matrix[submarine_position[0]][submarine_position[1]] == '*':
        submarine_health -= 1
        matrix[submarine_position[0]][submarine_position[1]] = 'S'
        if submarine_health < 0:
            print(f"Mission failed, U-9 disappeared! Last known coordinates"
                  f" [{submarine_position[0]}, {submarine_position[1]}]!")
            break
    elif matrix[submarine_position[0]][submarine_position[1]] == 'C':
        destroyed_cruisers += 1
        matrix[submarine_position[0]][submarine_position[1]] = 'S'
        if destroyed_cruisers == 3:
            print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
            break

for row in matrix:
    print(*row, sep='')
