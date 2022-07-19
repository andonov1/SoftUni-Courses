from math import floor
record_seconds = float(input())
distance_meters = float(input())
time_for_1_m = float(input())
slowing_per_m = floor(distance_meters / 50) * 30

my_time = (distance_meters * time_for_1_m) + slowing_per_m
if my_time < record_seconds:
    print(f" Yes! The new record is {my_time:.2f} seconds.")
else:
    print(f"No! He was {my_time - record_seconds:.2f} seconds slower.")