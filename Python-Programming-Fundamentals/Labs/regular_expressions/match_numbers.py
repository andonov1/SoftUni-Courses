import re

pattern = r"(^|(?<=\s))-?\d+(\.\d+)?($|(?=\s))"
text = input()
matches = re.finditer(pattern, text)
matches = [num.group() for num in matches]
print(*matches)