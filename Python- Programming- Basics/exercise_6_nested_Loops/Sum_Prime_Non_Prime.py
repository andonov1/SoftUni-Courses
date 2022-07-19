from math import sqrt
from math import ceil
prime_num = 0
non_prime_num = 0
command = input()

while command != 'stop':
    curr_num = int(command)
    if curr_num < 0:
        print("Number is negative.")
        command = input()
        continue
    if curr_num <= 1:
        non_prime_num += curr_num
    else:
        is_prime = True
        for div in range(2, ceil(sqrt(curr_num))):
            if curr_num % div == 0:
                is_prime = False
                break
        if is_prime:
            prime_num += curr_num
        else:
            non_prime_num += curr_num
    command = input()
print(f"Sum of all prime numbers is: {prime_num}")
print(f"Sum of all non prime numbers is: {non_prime_num}")
