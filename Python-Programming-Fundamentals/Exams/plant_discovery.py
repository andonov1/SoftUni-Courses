n = int(input())
plants = {}

for i in range(n):
    command = input().split('<->')
    plant = command[0]
    rarity = int(command[1])
    plants[plant] = [rarity]

while True:
    command = input().split(': ')
    if command[0] == 'Exhibition':
        break
    elif command[0] == 'Rate':
        data = command[1].split(' - ')
        plant = data[0]
        rating = int(data[1])
        if plant in plants:
            plants[plant].append(rating)
        else:
            print("error")
    elif command[0] == "Update":
        data = command[1].split(' - ')
        plant = data[0]
        new_rarity = int(data[1])
        if plant in plants:
            plants[plant][0] = new_rarity
        else:
            print("error")
    else:
        plant = command[1]
        if plant in plants:
            plants[plant] = [plants[plant][0]]
        else:
            print("error")

print("Plants for the exhibition:")
for key, value in plants.items():
    if len(value) > 1:
        total_sum = sum(value[1:])
        average_rating = total_sum / (len(value) - 1)
        print(f'- {key}; Rarity: {value[0]}; Rating: {average_rating:.2f}')
    else:
        print(f'- {key}; Rarity: {value[0]}; Rating: 0.00')
