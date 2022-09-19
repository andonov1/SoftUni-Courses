def logged(func):
    def wrapper(*args):
        result = f'you called {func.__name__}({", ".join([str(s) for s in args])})\n'
        result += f'it returned {func(*args)}'
        return result

    return wrapper


@logged
def func(*args):
    return 3 + len(args)


print(func(4, 4, 4))
