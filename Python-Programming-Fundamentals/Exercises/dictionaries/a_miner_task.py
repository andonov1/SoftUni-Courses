command = input()
data = []
quantities_dict = {}
while command != 'stop':
    data.append(command)
    command = input()

for i in range(0, len(data), 2):
    if data[i] not in quantities_dict:
        quantities_dict[data[i]] = int(data[i + 1])
    else:
        quantities_dict[data[i]] += int(data[i + 1])
[print(f"{resource} -> {quantity}") for resource, quantity in quantities_dict.items()]