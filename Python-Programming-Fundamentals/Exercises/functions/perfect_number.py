def is_aliquot(number):
    aliquot_sum = 0
    for i in range(1, number):
        if number % i == 0:
            aliquot_sum += i
    if aliquot_sum == number:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."


given_number = int(input())
print(is_aliquot(given_number))
