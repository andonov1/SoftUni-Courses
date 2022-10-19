max_health = 100
health = max_health
bitcoins = 0
rooms = input().split("|")
rooms_cnt = 0

for room in rooms:
    rooms_cnt += 1
    room = room.split()
    command = room[0]
    number = int(room[1])
    if command == 'potion':
        if health + number > max_health:
            health_points = max_health - health
            health = max_health
        else:
            health_points = number
            health += health_points
        print(f'You healed for {health_points} hp.')
        print(f'Current health: {health} hp.')
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            print(f"You died! Killed by {command}.")
            print(f"Best room: {rooms_cnt}")
            exit()

print(f"You've made it!\nBitcoins: {bitcoins}\nHealth: {health}")
