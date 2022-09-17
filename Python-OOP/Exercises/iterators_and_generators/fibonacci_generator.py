def fibonacci():
    fib0 = 0
    fib1 = 1

    yield fib0
    yield fib1

    while True:
        next_number = fib1 + fib0
        yield next_number
        fib0 = fib1
        fib1 = next_number


generator = fibonacci()

for i in range(5):
    print(next(generator))
