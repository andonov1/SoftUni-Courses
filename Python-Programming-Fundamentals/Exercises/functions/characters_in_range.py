def characters_in_range(start, end):
    all_characters = []
    for i in range(ord(start)+1, ord(end)):
        all_characters.append(chr(i))
    return all_characters


first_string = input()
second_string = input()
print(" ".join(characters_in_range(first_string, second_string)))
