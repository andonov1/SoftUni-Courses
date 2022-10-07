import sys
d = {1: 'a', 2: 'b', 3: 'c', 4: 'a', 5: 'd', 6: 'e', 7: 'a', 8: 'b'}
result = []
searched_value = sys.argv[1]
for key, value in d.items():
    if value == searched_value:
        result.append(key)
print(result, end='')