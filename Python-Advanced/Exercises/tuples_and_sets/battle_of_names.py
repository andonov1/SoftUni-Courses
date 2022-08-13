n = int(input())
odd = set()
even = set()
odd_sum = 0
even_sum = 0

for row in range(1, n + 1):
    name = sum([ord(x) for x in input()]) // row
    if name % 2 == 0:
        even.add(name)
        even_sum += name
    else:
        odd.add(name)
        odd_sum += name
if odd_sum == even_sum:
    result = odd.union(even)
elif odd_sum > even_sum:
    result = odd.difference(even)
else:
    result = odd.symmetric_difference(even)

print(*result, sep=', ')