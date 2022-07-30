from math import ceil
num_people = int(input())
capacity = int(input())
course = ceil(num_people / capacity)
print(course)