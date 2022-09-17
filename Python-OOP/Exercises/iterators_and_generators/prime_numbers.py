def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_primes(numbers):
    for num in numbers:
        if is_prime(num):
            yield num


print(list(get_primes([-2, 0, 0, 1, 1, 0])))
