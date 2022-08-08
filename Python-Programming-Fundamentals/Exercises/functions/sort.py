def sorted_numbers(numbers):
    integer_numbers = []
    for i in numbers:
        integer_numbers.append(int(i))
    return sorted(integer_numbers)


given_nums = input().split()
print(sorted_numbers(given_nums))