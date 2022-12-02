import re

pattern = r'(?P<separator>[\#|\|])(?P<item>[A-Z a-z]+)(?P=separator)(?P<date>[0-9]{2}\/[0-9]{2}\/[0-9]{2})(' \
          r'?P=separator)' \
          r'(?P<calories>\d+)(?P=separator)'
sentence = input()
total_calories = 0
items = {}
result = ''

valid_items = re.findall(pattern, sentence)
for item in valid_items:
    result += f"Item: {item[1]}, Best before: {item[2]}, Nutrition: {item[3]}\n"
    total_calories += int(item[3])

print(f"You have food to last you for: {int(total_calories / 2000)} days!")
print(result)
