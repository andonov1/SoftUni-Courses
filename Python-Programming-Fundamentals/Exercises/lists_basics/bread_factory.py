initial_energy = 100
initial_coins = 100
events = input().split('|')
shop_open = True
for event in events:
    current_event = event.split('-')
    type_event = current_event[0]
    number = int(current_event[1])
    if type_event == 'rest':
        temporary_energy = initial_energy
        initial_energy += number
        if initial_energy > 100:
            initial_energy = 100
        gained_energy = initial_energy - temporary_energy
        print(f"You gained {gained_energy} energy.")
        print(f"Current energy: {initial_energy}.")
    elif type_event == 'order':
        if initial_energy >= 30:
            initial_energy -= 30
            initial_coins += number
            print(f"You earned {number} coins.")
        else:
            initial_energy += 50
            print(f"You had to rest!")
    else:
        initial_coins -= number
        if initial_coins >= 0:
            print(f"You bought {type_event}.")
        else:
            shop_open = False
            print(f"Closed! Cannot afford {type_event}.")
if shop_open:
    print(f'Day completed!\n'
          f'Coins: {initial_coins}\n'
          f'Energy: {initial_energy}')
