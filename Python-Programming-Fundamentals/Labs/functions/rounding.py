def rounding(numbers):
    rounded_float_numbers = []
    for i in numbers:
        rounded_float_numbers.append(round(float(i)))
    return rounded_float_numbers


string_numbers = input().split()
print(rounding(string_numbers))