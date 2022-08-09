houses = [int(x) for x in input().split('@')]
command = input()
current_index = 0
while command != 'Love!':
    action = command.split()
    jump_len = int(action[1])
    current_index += jump_len
    if current_index >= len(houses):
        current_index = 0
    if houses[current_index] == 0:
        print(f"Place {current_index} already had Valentine's day.")
    else:
        houses[current_index] -= 2
        if int(houses[current_index]) <= 0:
            houses[current_index] = 0
            print(f"Place {current_index} has Valentine's day.")

    command = input()
print(f"Cupid's last position was {current_index}.")
house_cnt = houses.count(0)
if house_cnt == len(houses):
    print("Mission was successful.")
else:
    print(f'Cupid has failed {len(houses) - house_cnt} places.')
