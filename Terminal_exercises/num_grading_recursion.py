import sys


def num_pow(num, rate):
    if rate == 0:
        return 1
    return num * num_pow(num, rate - 1)


num = int(sys.argv[1])
rate = int(sys.argv[2])
print(num_pow(num, rate))
