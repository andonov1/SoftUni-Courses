import sys
from math import sqrt


def get_roots(a, b, c):
    if a == 0 or b == 0 or c == 0:
        return "special case"
    d = (b ** 2) - (4 * a * c)
    if d < 0:
        return "no real roots"
    elif d == 0:
        x1 = -b / (2 * a)
        return x1
    else:
        x1 = (-b + sqrt(d)) / (2 * a)
        x2 = (-b - sqrt(d)) / (2 * a)
        return f"{x1}|{x2}"


a, b, c = float(sys.argv[1]), float(sys.argv[2]), float(sys.argv[3])
print(get_roots(a, b, c), end='')
