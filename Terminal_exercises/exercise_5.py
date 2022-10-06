import sys

given_list = [int(s) for s in sys.argv[1:]]

result = list(set(given_list))
print(result, end='')
