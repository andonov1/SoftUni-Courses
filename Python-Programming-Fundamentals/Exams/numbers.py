given_arr = [int(s) for s in input().split()]
top_5_number_greater_than_avg = []

avg = sum(given_arr) / len(given_arr)
needed_nums = 5

for num in sorted(given_arr, reverse=True):
    if needed_nums == 0:
        break
    if num > avg:
        top_5_number_greater_than_avg.append(num)
        needed_nums -= 1

if not top_5_number_greater_than_avg:
    print('No')
else:
    print(' '.join(str(x) for x in sorted(top_5_number_greater_than_avg, reverse=True)))
