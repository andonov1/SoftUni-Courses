from collections import deque

bowls = [int(s) for s in input().split(', ')]
customers = deque([int(s) for s in input().split(', ')])

while bowls and customers:
    bowl = bowls.pop()
    customer = customers.popleft()

    if bowl == customer:
        continue
    elif bowl > customer:
        bowl -= customer
        bowls.append(bowl)
    else:
        customer -= bowl
        customers.appendleft(customer)

if not customers:
    print("Great job! You served all the customers.")
    if bowls:
        print(f"Bowls of ramen left: {', '.join(str(s) for s in bowls)}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(str(s) for s in customers)}")