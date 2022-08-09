first_strings = input().split(', ')
second_strings = input().split(', ')
substrings = []
for first_words in first_strings:
    for second_word in second_strings:
        if first_words in second_word:
            substrings.append(first_words)
            break
print(substrings)