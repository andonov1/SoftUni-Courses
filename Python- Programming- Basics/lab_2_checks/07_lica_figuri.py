from math import pi
form = input()
area = 0
if form == "square":
    a = float(input())
    area = (a * a)
elif form == "rectangle":
    a = float(input())
    b = float(input())
    area = (a * b)
elif form == "triangle":
    a = float(input())
    b = float(input())
    area = (1/2 * a * b)
elif form == "circle":
    r = float(input())
    area = pi * (r ** 2)
print(f'{area:.3f}')


