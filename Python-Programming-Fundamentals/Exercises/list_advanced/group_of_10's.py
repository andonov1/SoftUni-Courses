import math

numbers = [int(i) for i in input().split(', ')]
groups = math.ceil(max(numbers) / 10)
min = 1
max = 10
for group in range(1, groups + 1):
    print(f"Group of {group*10}'s: {[x for x in numbers if min <= x <= max]}")
    min += 10
    max += 10
