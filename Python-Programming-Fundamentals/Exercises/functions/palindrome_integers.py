def palindrome_numbers(numbers):
    for i in numbers:
        is_palindrome = True
        temp_num = i
        reversed_num = 0
        while i != 0:
            digit = i % 10
            reversed_num = reversed_num * 10 + digit
            i //= 10
        if reversed_num != temp_num:
            is_palindrome = False
        print(is_palindrome)


numbers_as_digits = [int(s) for s in input().split(', ')]
palindrome_numbers(numbers_as_digits)
