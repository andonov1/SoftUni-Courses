import sys


def palindrome(text, inx=0):
    if inx == len(text) // 2:
        return True

    if text[inx] != text[0 - inx - 1]:
        return False
    return palindrome(text, inx + 1)


word = sys.argv[1]
print(palindrome(word))
