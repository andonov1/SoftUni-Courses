from collections import deque

person_caffeine = 0
caffeine = [int(s) for s in input().split(', ')]
energy_drinks = deque(int(s) for s in input().split(', '))

while caffeine and energy_drinks:
    current_caffeine = caffeine.pop()
    current_drink = energy_drinks.popleft()
    current_power = current_drink * current_caffeine
    if current_power + person_caffeine <= 300:
        person_caffeine += current_power
    else:
        energy_drinks.append(current_drink)
        person_caffeine -= 30
        if person_caffeine < 0:
            person_caffeine = 0

if energy_drinks:
    print(f"Drinks left: {', '.join(str(s) for s in energy_drinks)}")
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f"Stamat is going to sleep with {person_caffeine} mg caffeine.")