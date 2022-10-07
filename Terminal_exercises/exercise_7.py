import sys


def caesar_cipher(text: str, key: int):
    result = ""
    for i in range(len(text)):
        char = text.lower()[i]
        result += chr((ord(char) + key - 97) % 26 + 97)
    return result.upper()


def vigenere_cipher(text: str, key: str):
    result = ""
    for i in range(len(text)):
        char = text.lower()[i]
        shifted_letter = key.lower()[i % len(key)]
        shift = ord(shifted_letter) - 97
        result += caesar_cipher(char, shift)
    return result.upper()


text = sys.argv[1]
key = sys.argv[2]
print(vigenere_cipher(text, key))

