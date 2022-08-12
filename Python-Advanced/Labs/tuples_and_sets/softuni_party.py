n = int(input())
reservations = set()

for _ in range(n):
    guest = input()
    reservations.add(guest)

command = input()

while command != 'END':
    if command in reservations:
        reservations.remove(command)
    command = input()

print(len(reservations))
print('\n'.join(sorted(reservations)))