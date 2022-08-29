first_line = set([int(s) for s in input().split()])
second_line = set([int(s) for s in input().split()])
n = int(input())

for _ in range(n):
    command = input().split()

    if command[0] == 'Add':
        if command[1] == 'First':
            [first_line.add(int(x)) for x in command[2:]]
        else:
            [second_line.add(int(x)) for x in command[2:]]

    elif command[0] == 'Remove':
        if command[1] == 'First':
            first_line = first_line.difference([int(x) for x in command[2:]])
        else:
            second_line = second_line.difference([int(x) for x in command[2:]])

    else:
        print(first_line.issubset(second_line) or second_line.issubset(first_line))

first_line = sorted(first_line)
second_line = sorted(second_line)
print(', '.join([str(s) for s in first_line]))
print(', '.join([str(s) for s in second_line]))