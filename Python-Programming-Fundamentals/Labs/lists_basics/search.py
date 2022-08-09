n = int(input())
given_word = input()
all_words = []
including_words = []
for _ in range(n):
    word = input()
    all_words.append(word)
    if given_word in word:
        including_words.append(word)
print(all_words)
print(including_words)