import sys

stem_file_name = sys.argv[1]
word = sys.argv[2]
result = {}

with open(stem_file_name, 'r') as f:
    for line in f:
        line = line.split(':')
        result[line[0]] = line[1]
if word in result:
    print(result[word])