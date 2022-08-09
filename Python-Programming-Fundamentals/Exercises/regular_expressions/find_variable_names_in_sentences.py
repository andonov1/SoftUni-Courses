import re

pattern = r'\b_([A-Za-z0-9]+)\b'
lines = input()
matches = re.findall(pattern, lines)
print(','.join(matches))