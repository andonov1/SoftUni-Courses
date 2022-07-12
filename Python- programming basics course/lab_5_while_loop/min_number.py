import sys

min_number = sys.maxsize

while True:
    num = input()
    if num != 'Stop':
        num = int(num)
        if num <= min_number:
            min_number = num
    else:
        print(min_number)
        break
