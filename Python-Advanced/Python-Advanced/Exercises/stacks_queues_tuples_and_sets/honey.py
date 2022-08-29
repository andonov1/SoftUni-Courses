from collections import deque

bees = deque([int(x) for x in input().split()])
nectars = [int(x) for x in input().split()]
operators = deque([x for x in input().split()])

collected_nectar = 0

while bees and nectars:
    current_bee = bees.popleft()
    current_nectar = nectars.pop()
    if current_nectar >= current_bee:
        current_operator = operators.popleft()
        if current_operator == '+':
            collected_nectar += current_bee + current_nectar
        elif current_operator == '-':
            collected_nectar += abs(current_bee - current_nectar)
        elif current_operator == '*':
            collected_nectar += current_bee + current_nectar
        elif current_operator == '/' and current_nectar > 0:
            collected_nectar += abs(current_bee / current_nectar)
    else:
        bees.appendleft(current_bee)

print(f"Total honey made: {collected_nectar}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectars:
    print(f"Nectar left: {', '.join([str(x) for x in nectars])}")