first_word, second_word = input().split()
shorter_word = min(len(first_word), len(second_word))
total_sum = 0

for i in range(shorter_word):
    total_sum += ord(first_word[i]) * ord(second_word[i])

longest_word = max(len(first_word), len(second_word))

for i in range(shorter_word, longest_word):
    if len(first_word) > len(second_word):
        total_sum += ord(first_word[i])
    else:
        total_sum += ord(second_word[i])

print(total_sum)
