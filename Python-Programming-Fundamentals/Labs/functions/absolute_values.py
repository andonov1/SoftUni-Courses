nums = input().split()
integers = []
for i in nums:
    number = float(i)
    integers.append(number)
absolute_values = []
for n in integers:
    absolute_number = abs(n)
    absolute_values.append(absolute_number)
print(absolute_values)