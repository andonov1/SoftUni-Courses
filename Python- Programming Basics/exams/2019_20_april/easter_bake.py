import sys
from math import ceil
num_kozunaks = int(input())
required_sugar = 0
required_flour = 0
max_sugar = -sys.maxsize
max_flour = -sys.maxsize
for i in range(num_kozunaks):
    used_sugar = int(input())
    used_flour = int(input())
    required_sugar += used_sugar
    required_flour += used_flour
    if used_sugar > max_sugar:
        max_sugar = used_sugar
    if used_flour > max_flour:
        max_flour = used_flour
packs_sugar = ceil(required_sugar / 950)
packs_flour = ceil(required_flour / 750)
print(f"Sugar: {packs_sugar}")
print(f"Flour: {packs_flour}")
print(f"Max used flour is {max_flour} grams, max used sugar is {max_sugar} grams.")