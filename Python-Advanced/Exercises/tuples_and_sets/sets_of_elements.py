n, m = input().split()
n, m = int(n), int(m)
first_set = set()
second_set = set()

for _ in range(n):
    number = input()
    first_set.add(number)
for _ in range(m):
    number = input()
    second_set.add(number)

print(*first_set.intersection(second_set), sep='\n')