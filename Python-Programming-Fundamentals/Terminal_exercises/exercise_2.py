import sys

params = sys.argv[1:]
is_sorted = True

for i in range(1, len(params)):
    if params[i] < params[i - 1]:
        is_sorted = False
        break

if is_sorted:
    print('sorted', end='')
else:
    print('unsorted', end='')
