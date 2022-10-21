import sys

file_to_sort = sys.argv[1]
new_file_name = sys.argv[2]

file = open(new_file_name, 'w')
with open(file_to_sort, 'r') as f:
    for line in sorted(f):
        file.write(line)
file.close()
