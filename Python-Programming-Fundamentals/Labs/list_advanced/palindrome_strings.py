string_words = input().split()
palindrome = input()

palindrome_words = [x for x in string_words if x == x[:: -1]]
print(palindrome_words)
print(f"Found palindrome {palindrome_words.count(palindrome)} times")