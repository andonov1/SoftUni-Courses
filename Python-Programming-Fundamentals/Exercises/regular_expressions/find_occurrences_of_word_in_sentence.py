import re

line = input()
searched_word = input()
pattern = fr'\b{searched_word}\b'
matches = re.findall(pattern, line, flags=re.IGNORECASE)
print(len(matches))
