n = int(input())
total = 0
for char in range(n):
    current_char = input()
    total += ord(current_char)
print(f"The sum equals: {total}")