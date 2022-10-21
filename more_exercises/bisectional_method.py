import math


def f(x):
    return math.pow(x, 3) + 3 * x - 5


def f1(x):
    return pow(math.e, x) - 2 * x - 2


def bisection(a, b, func):
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        return 'a and b must be numbers!'

    if func(a) * func(b) >= 0:
        raise Exception('a and b must have opposite signs!')

    while (b - a) >= 0.1:
        c = (a + b) / 2
        if func(c) == 0:
            break
        if func(c) * func(a) < 0:
            b = c
        elif func(c) * func(b) < 0:
            a = c
    return f'{c:.3f}'
