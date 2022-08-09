groceries = input().split('!')
command = input()
while command != 'Go Shopping!':
    message = command.split()
    if message[0] == 'Urgent':
        if message[1] not in groceries:
            groceries.insert(0, message[1])
    elif message[0] == 'Unnecessary':
        if message[1] in groceries:
            groceries.remove(message[1])
    elif message[0] == 'Correct':
        if message[1] in groceries:
            index = groceries.index(message[1])
            groceries[index] = message[2]
    elif message[0] == 'Rearrange':
        if message[1] in groceries:
            groceries.remove(message[1])
            groceries.append(message[1])
    command = input()
print(", ".join(groceries))
