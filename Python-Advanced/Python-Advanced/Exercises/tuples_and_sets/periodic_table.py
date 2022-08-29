n = int(input())
unique_chemicals = set()

for _ in range(n):
    line = input().split()
    for chemical in line:
        unique_chemicals.add(chemical)

print(*unique_chemicals, sep='\n')