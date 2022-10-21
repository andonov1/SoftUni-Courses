import sys

first_word, second_word = sys.argv[1:]
words_are_anagrams = True

if sorted(first_word.lower()) != sorted(second_word.lower()):
    words_are_anagrams = False

print(words_are_anagrams, end='')
