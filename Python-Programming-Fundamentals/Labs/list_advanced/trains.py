num_wagons = int(input())
wagons = [0] * num_wagons
command = input()

while command != 'End':
    data = command.split()
    if data[0] == 'add':
        wagons[-1] += int(data[1])
    elif data[0] == 'insert':
        index = int(data[1])
        n_people = int(data[2])
        wagons[index] += n_people
    elif data[0] == 'leave':
        index = int(data[1])
        n_people = int(data[2])
        wagons[index] -= n_people
    command = input()

print(wagons)
