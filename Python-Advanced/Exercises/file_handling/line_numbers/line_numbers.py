import re

with open('text.txt', 'r') as file, open('output_file.txt', 'w') as output_file:
    result = ''
    for row, line in enumerate(file):
        stripped_line = line.strip()
        letters_cnt = len(re.findall('[A-Za-z]', stripped_line))
        punctuation_marks = len(re.findall('[,.\\-\'":?!]', stripped_line))
        output_file.write(f'Line {row}: {stripped_line} ({letters_cnt})({punctuation_marks})\n')


