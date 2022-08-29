unique_names = set()
n = int(input())
for _ in range(n):
    name = input()
    unique_names.add(name)

print("\n".join(unique_names))