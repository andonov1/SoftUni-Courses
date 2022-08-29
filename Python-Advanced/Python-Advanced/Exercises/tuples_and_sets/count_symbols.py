line = input()
occurrences = {}

for char in line:
    if char not in occurrences:
        occurrences[char] = 1
    else:
        occurrences[char] += 1

for key, value in sorted(occurrences.items()):
    print(f'{key}: {value} time/s')
