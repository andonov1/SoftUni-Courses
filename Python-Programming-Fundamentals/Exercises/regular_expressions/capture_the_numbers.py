import re
lines = input()
pattern = r'\d+'
while True:
    if lines:
        matches = re.findall(pattern, lines)
        if matches:
            print(' '.join(matches), end=' ')
    else:
        break
    lines = input()