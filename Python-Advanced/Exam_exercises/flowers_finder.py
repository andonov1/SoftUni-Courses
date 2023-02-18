from collections import deque

vowels = deque([s for s in input().split()])
consonants = [s for s in input().split()]
found_word = False
words = {"rose": [],
         "tulip": [],
         "lotus": [],
         "daffodil": []}

while vowels and consonants:
    if found_word:
        break
    vowel = vowels.popleft()
    consonant = consonants.pop()
    for word in words:
        if vowel in word and vowel not in words[word]:
            for i in range(word.count(vowel)):
                words[word].append(vowel)
        if consonant in word and consonant not in words[word]:
            for i in range(word.count(consonant)):
                words[word].append(consonant * word.count(consonant))
        if len(word) <= len(words[word]):
            print(f"Word found: {word}")
            found_word = True
            break


if not found_word:
    print("Cannot find any word!")
if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")