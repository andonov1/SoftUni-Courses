def cache(func):
    log = {}

    def wrapper(n):
        if n in log:
            return log[n]
        result = func(n)
        log[n] = result
        wrapper.log = log
        return result

    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


fibonacci(3)

print(fibonacci.log)
