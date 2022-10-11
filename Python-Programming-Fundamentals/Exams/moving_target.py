def index_valid(inx, list):
    if 0 <= inx < len(list):
        return True
    return False


targets = [int(s) for s in input().split()]

while True:
    command = input()
    if command == "End":
        break
    command = command.split()
    action = command[0]
    inx = int(command[1])
    value = int(command[2])
    if action == 'Shoot':
        if index_valid(inx, targets):
            targets[inx] -= value
            if targets[inx] <= 0:
                targets.pop(inx)
    elif action == 'Add':
        if index_valid(inx, targets):
            targets.insert(inx, value)
        else:
            print("Invalid placement!")
    else:
        if index_valid(inx, targets) and index_valid(inx + value, targets) and index_valid(inx - value, targets):
            targets = targets[:inx - value] + targets[inx + value + 1::]
        else:
            print("Strike missed!")

print('|'.join(str(s) for s in targets))