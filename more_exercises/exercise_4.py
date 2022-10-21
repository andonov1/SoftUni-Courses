import sys

given_list = sys.argv[1:]
list_has_identical_chars = False

for el in given_list:
    if given_list.count(el) > 1:
        list_has_identical_chars = True

print(list_has_identical_chars, end='')
