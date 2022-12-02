import re

text = input()
pattern = r'(?P<separator>@|#)(?P<first_word>[A-z]{3,})(?P=separator)(?P=separator)(?P<second_word>[A-z]{3,})' \
          r'(?P=separator)'
valid_pairs = []
mirror_words = []

for match in re.finditer(pattern, text):
    valid_pairs.append(match.group())
    data = match.groupdict()
    first_word = data['first_word']
    second_word = data['second_word']
    if second_word[::-1] == first_word:
        mirror_words.append([first_word, second_word])
if valid_pairs:
    print(f"{len(valid_pairs)} word pairs found!")
else:
    print("No word pairs found!")
if mirror_words:
    print(f"The mirror words are:")
    for word in mirror_words:
        if word != mirror_words[-1]:
            print(f"{word[0]} <=> {word[1]}", end=', ')
        else:
            print(f"{word[0]} <=> {word[1]}")
else:
    print("No mirror words!")
