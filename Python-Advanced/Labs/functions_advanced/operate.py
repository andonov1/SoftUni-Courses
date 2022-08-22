def operate(operator, *args):
    if operator in ('+', '-'):
        result = 0
    else:
        result = 1
    if operator == '+':
        for el in args:
            result += el
    elif operator == '-':
        for el in args:
            result -= el
    elif operator == '*':
        for el in args:
            result *= el
    elif operator == '/':
        for el in args:
            result /= el
    return result
print(operate("*", 0, 1))