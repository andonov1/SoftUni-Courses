from collections import deque

chocolates = [int(s) for s in input().split(', ')]
cups_of_milk = deque([int(s) for s in input().split(', ')])
milkshakes = 0

while milkshakes < 5 and chocolates and cups_of_milk:
    current_chocolate = chocolates.pop()
    current_cup = cups_of_milk.popleft()
    if current_chocolate <= 0 and current_cup <= 0:
        continue
    elif current_chocolate <= 0:
        cups_of_milk.appendleft(current_cup)
        continue
    elif current_cup <= 0:
        chocolates.append(current_chocolate)
        continue

    if current_chocolate == current_cup:
        milkshakes += 1
    else:
        cups_of_milk.append(current_cup)
        chocolates.append(current_chocolate - 5)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(str(s) for s in chocolates)}")
else:
    print("Chocolate: empty")
if cups_of_milk:
    print(f"Milk: {', '.join(str(s) for s in cups_of_milk)}")
else:
    print("Milk: empty")
