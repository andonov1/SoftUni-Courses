import sys

max_number = -sys.maxsize

while True:
    num = input()
    if num != 'Stop':
        num = int(num)
        if num >= max_number:
            max_number = num
    else:
        print(max_number)
        break






