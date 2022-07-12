first_player_name = input()
second_player_name = input()
first_player_pts = 0
second_player_pts = 0
command1 = input()
while command1 != 'End of game':
    command2 = int(input())
    player1_pts = int(command1)
    player2_pts = command2
    if player1_pts > player2_pts:
        first_player_pts += (player1_pts - player2_pts)
    if player2_pts > player1_pts:
        second_player_pts += (player2_pts - player1_pts)
    if player1_pts == player2_pts:
        print("Number wars!")
        command1 = int(input())
        command2 = int(input())
        if command1 > command2:
            print(f"{first_player_name} is winner with {first_player_pts} points")
            break
        elif command1 < command2:
            print(f"{second_player_name} is winner with {second_player_pts} points")
            break
    command1 = input()
if command1 == 'End of game':
    print(f'{first_player_name} has {first_player_pts} points')
    print(f'{second_player_name} has {second_player_pts} points')
