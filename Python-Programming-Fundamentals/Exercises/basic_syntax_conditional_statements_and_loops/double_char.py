command = input()
while command != 'End':
    current_string = ''
    for i in range(len(command)):
        current_string += command[i] * 2
    if command != "SoftUni":
        print(current_string)
    command = input()