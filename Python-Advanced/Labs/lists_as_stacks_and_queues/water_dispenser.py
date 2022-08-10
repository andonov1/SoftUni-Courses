from collections import deque
liter = int(input())
name = input()
line = deque()
while not name == 'Start':
    line.append(name)
    name = input()
command = input()

while not command == 'End':
    if command.isdigit():
        required_liters = int(command)
        name = line.popleft()
        if required_liters <= liter:
            liter -= required_liters
            print(f'{name} got water')
        else:
            print(f'{name} must wait')

    else:
        _, refill = command.split()
        refill = int(refill)
        liter += refill
    command = input()
print(f'{liter} liters left')