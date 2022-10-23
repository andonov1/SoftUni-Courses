from math import ceil

budget = float(input())
students = int(input())
price_package_flour = float(input())
price_per_egg = float(input())
price_per_apron = float(input())

required_budget = (price_per_apron * ceil(students * 1.2)) + (price_per_egg * 10 * students) + \
(price_package_flour * ceil(students - students // 5))

if required_budget <= budget:
    print(f'Items purchased for {required_budget:.2f}$.')
else:
    print(f'{required_budget - budget:.2f}$ more needed.')