def sum_of_digits(number):
    sum_of_odd_digits = 0
    sum_of_even_digits = 0
    for i in range(0, len(number)):
        if int(number[i]) % 2 == 0:
            sum_of_even_digits += int(number[i])
        else:
            sum_of_odd_digits += int(number[i])

    print(f"Odd sum = {sum_of_odd_digits}, Even sum = {sum_of_even_digits}")


given_number = input()
sum_of_digits(given_number)
