number = int(input())

total_even = 0
total_odd = 0
for num in range(1, number + 1):
    current_number = int(input())
    if num % 2 == 0:
        total_even += current_number
    if num % 2 != 0:
        total_odd += current_number
diff = abs(total_even - total_odd)
if total_even == total_odd:
    print('Yes')
    print(f'Sum = {total_even}')
else:
    print('No')
    print(f'Diff = {diff}')