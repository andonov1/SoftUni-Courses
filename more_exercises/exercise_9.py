import sys
text = sys.argv[1]
d = {}
for el in text:
    if el in d:
        d[el] += 1
    else:
        d[el] = 1
result = []
for key, value in d.items():
    result.append((key, value))
print(result, end="")