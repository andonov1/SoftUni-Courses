def words_sorting(*args):
    words = {}
    total_sum = 0
    result = ''
    for el in args:
        ascii_value = 0
        for letter in el:
            ascii_value += ord(letter)
        words[el] = ascii_value
        total_sum += ascii_value

    if total_sum % 2 != 0:
        sorted_words = {k: v for k, v in sorted(words.items(), key=lambda x: (-x[1]))}
    else:
        sorted_words = {k: v for k, v in sorted(words.items(), key=lambda x: (x[0]))}

    for key, value in sorted_words.items():
        result += f"{key} - {value}\n"
    return result


print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
    ))
