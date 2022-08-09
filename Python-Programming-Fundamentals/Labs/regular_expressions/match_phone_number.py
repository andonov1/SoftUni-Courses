import re

pattern = r"(\+359 2 \d{3} \d{4})|(\+359-2-\d{3}-\d{4})\b"
text = input()

matches = re.finditer(pattern, text)
valid_numbers = [phone.group() for phone in matches]

print(', '.join(valid_numbers))
