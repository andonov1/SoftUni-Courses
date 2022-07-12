cake_lenght = int(input())
cake_width = int(input())

pieces_left = cake_lenght * cake_width
curr_command = input()
while curr_command != 'STOP':
    pieces_taken = int(curr_command)
    pieces_left -= pieces_taken
    if pieces_left < 0:
        break
    curr_command = input()
if curr_command == 'STOP':
    print(f"{pieces_left} pieces are left.")
else:
    print(f'No more cake left! You need {abs(pieces_left)} pieces more.')
