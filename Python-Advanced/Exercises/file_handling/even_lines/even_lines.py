symbols = ["-", ",", ".", "!", "?"]

with open('text.txt', 'r') as file:
    for row, line in enumerate(file):
        if row % 2 == 0:
            result = ' '.join(reversed(line.strip().split()))
            for char in symbols:
                result = result.replace(char, '@')
            print(result)
