from collections import deque

n = int(input())
pumps = deque()

for _ in range(n):
    pumps_data = [int(x) for x in input().split()]
    pumps.append(pumps_data)

for attempt in range(n):
    tank = 0
    failed = False
    for petrol, distance in pumps:
        tank += petrol

        if distance > tank:
            failed = True
            break
        else:
            tank -= distance
    if failed:
        pumps.append((pumps.popleft()))
    else:
        print(attempt)
        break
