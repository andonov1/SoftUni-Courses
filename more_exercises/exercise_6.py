import sys


def caesar_cipher(text: str, key: int):
    result = ""
    for i in range(len(text)):
        char = text.lower()[i]
        result += chr((ord(char) + key - 97) % 26 + 97)
    return result.upper()


text = sys.argv[1]
key = int(sys.argv[2])
print(caesar_cipher(text, key))
