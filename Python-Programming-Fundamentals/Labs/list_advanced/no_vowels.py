given_string = input()
vowels = ['a', 'o', 'u', 'e', 'i']
no_vowels = ''.join([x for x in given_string if not x in vowels])
print(no_vowels)