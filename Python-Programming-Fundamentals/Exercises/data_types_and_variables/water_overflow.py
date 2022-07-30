capacity = 255
lines = int(input())
filled = 0
for i in range(lines):
    current_liters = int(input())
    if current_liters > capacity:
        print("Insufficient capacity!")
        continue
    capacity -= current_liters
    filled += current_liters
print(filled)