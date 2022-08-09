gifts = input().split()
command = input()
while command != "No Money":
    command1 = command.split()
    if command1[0] == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == command1[1]:
                gifts[i] = "None"
    if command1[0] == "Required":
        index = int(command1[2])
        if index >= 0 and index < len(gifts):
            gifts[index] = command1[1]
    if command1[0] == "JustInCase":
        gifts.pop()
        gifts.insert(len(gifts), command1[1])
    command = input()
for i in range(len(gifts)):
    if gifts[i] != 'None':
        print(f'{gifts[i]} ', end='')
