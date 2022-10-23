numbers = [int(s) for s in input().split()]

while True:
    command = input().split()
    if command[0] == "Finish":
        break
    elif command[0] == "Add":
        numbers.append(int(command[1]))
    elif command[0] == "Remove":
        if int(command[1]) in numbers:
            numbers.remove(int(command[1]))
    elif command[0] == "Replace":
        if int(command[1]) in numbers:
            inx = numbers.index(int(command[1]))
            numbers[inx] = int(command[2])
    else:
        for i in range(len(numbers) - 1, -1, -1):
            if numbers[int(i)] < int(command[1]):
                numbers.pop(int(i))

print(' '.join(str(s) for s in numbers))
