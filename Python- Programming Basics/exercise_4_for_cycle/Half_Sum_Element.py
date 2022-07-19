import sys
n = int(input())
max_number = -sys.maxsize
num_sum = 0

for i in range(0, n):
    current_number = int(input())
    if current_number > max_number:
        max_number = current_number
    num_sum += current_number
num_sum -= max_number
diff = abs(max_number - num_sum)
if max_number == num_sum:
    print('Yes')
    print(f'Sum = {max_number}')
else:
    print('No')
    print(f'Diff = {diff}')