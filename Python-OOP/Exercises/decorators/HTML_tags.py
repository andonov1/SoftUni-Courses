def tags(tag):
    def decorator(func):
        def wrapper(*args):
            func_result = func(*args)
            return f'<{tag}>{func_result}</{tag}>'

        return wrapper

    return decorator


@tags('p')
def join_strings(*args):
    return "".join(args)


print(join_strings("Hello", " you!"))
