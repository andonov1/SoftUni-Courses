def type_check(given_type):
    def decorator(func):
        def wrapper(given_info):
            if given_type == type(given_info):
                return func(given_info)
            return "Bad Type"
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num * 2


print(times2(2))

print(times2('Not A Number'))
