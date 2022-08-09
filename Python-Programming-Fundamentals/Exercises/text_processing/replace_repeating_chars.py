text = input()
result = ''
for char in text:
    if len(result) > 0 and result[-1] == char:
        continue
    else:
        result += char

print(result)