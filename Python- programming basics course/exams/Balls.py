import math

num = int(input())
red_cnt = 0
orange_cnt = 0
yellow_cnt = 0
white_cnt = 0
black_cnt = 0
total_pts = 0
other = 0
from math import floor
for i in range(num):
    color = input()
    if color == 'red':
        red_cnt += 1
        total_pts += 5
    elif color == 'orange':
        orange_cnt += 1
        total_pts += 10
    elif color == 'yellow':
        yellow_cnt += 1
        total_pts += 15
    elif color == 'white':
        white_cnt += 1
        total_pts += 20
    elif color == 'black':
        black_cnt += 1
        total_pts = math.floor(total_pts / 2)
    else:
        other += 1
        continue
print(f"Total points: {total_pts}")
print(f"Red balls: {red_cnt}")
print(f"Orange balls: {orange_cnt}")
print(f"Yellow balls: {yellow_cnt}")
print(f"White balls: {white_cnt}")
print(f"Other colors picked: {other}")
print(f"Divides from black balls: {black_cnt}")

