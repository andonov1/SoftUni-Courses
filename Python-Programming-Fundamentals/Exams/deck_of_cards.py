cards = input().split(', ')
n = int(input())

for i in range(n):
    command = input().split(', ')
    if command[0] == 'Add':
        if command[1] not in cards:
            cards.append(command[1])
            print('Card successfully added')
        else:
            print('Card is already in the deck')
    elif command[0] == 'Remove':
        if command[1] in cards:
            cards.remove(command[1])
            print('Card successfully removed')
        else:
            print('Card not found')
    elif command[0] == 'Remove At':
        inx = int(command[1])
        if 0 <= inx < len(cards):
            cards.pop(inx)
            print('Card successfully removed')
        else:
            print('Index out of range')
    else:
        inx = int(command[1])
        if 0 <= inx < len(cards):
            if command[2] in cards:
                print('Card is already added')
            else:
                cards.insert(inx, command[2])
                print('Card successfully added')
        else:
            print('Index out of range')

print(', '.join(cards))