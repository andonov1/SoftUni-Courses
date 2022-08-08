def min_max_sum(numbers):
    integers = []
    for i in numbers:
        integers.append(int(i))

    print(f"The minimum number is {min(integers)}")
    print(f"The maximum number is {max(integers)}")
    print(f"The sum number is: {sum(integers)}")


string_numbers = input().split()
min_max_sum(string_numbers)
