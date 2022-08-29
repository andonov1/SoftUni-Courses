from collections import deque

working = True
food_storage = int(input())
orders = deque([int(s) for s in input().split()])
print(max(orders))

while orders:
    if orders[0] <= food_storage:
        order_quantity = orders.popleft()
        food_storage -= order_quantity
    else:
        working = False
        break

if working:
    print(f'Orders complete')
else:
    print(f"Orders left: {' '.join([str(s) for s in orders])}")
