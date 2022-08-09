def even_words_function(words):
    return [print(x) for x in words if len(x) % 2 == 0]


even_words = input().split()
even_words_function(even_words)