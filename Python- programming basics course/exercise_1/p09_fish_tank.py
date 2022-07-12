lenght = int(input())
width = int(input())
height = int(input())
percent = float(input()) / 100

capacity = lenght * width * height
capacity_liters = capacity * 0.001
percent_capacity = capacity_liters * (1 - percent)
print(percent_capacity)
