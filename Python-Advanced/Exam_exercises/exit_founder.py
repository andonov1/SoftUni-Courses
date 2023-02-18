first_player, second_player = input().split(', ')
matrix = []
turn = 0
first_player_penalty = False
second_player_penalty = False

for i in range(6):
    matrix.append([s for s in input().split()])

while True:
    command = input().split(', ')
    row, col = int(command[0][1]), int(command[1][0])

    if turn % 2 == 0:
        player = first_player
        if first_player_penalty:
            first_player_penalty = False
            turn += 1
            continue
    else:
        player = second_player
        if second_player_penalty:
            second_player_penalty = False
            turn += 1
            continue
    turn += 1

    if matrix[row][col] == 'E':
        print(f"{player} found the Exit and wins the game!")
        break
    elif matrix[row][col] == "T":
        print(
            f"{player} is out of the game! The winner is {first_player if player == second_player else second_player}.")
        break
    elif matrix[row][col] == 'W':
        print(f"{player} hits a wall and needs to rest.")
        if player == first_player:
            first_player_penalty = True
        else:
            second_player_penalty = True
