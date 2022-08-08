def sum_numbers(n1, n2):
    return n1 + n2


def subtract(summed, n3):
    return summed - n3


def add_and_subtract(n1, n2, n3):
    return subtract(sum_numbers(n1, n2), n3)


num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
print(add_and_subtract(num_1, num_2, num_3))