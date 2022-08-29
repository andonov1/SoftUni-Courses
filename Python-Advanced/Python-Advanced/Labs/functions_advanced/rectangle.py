def rectangle(*args):
    def area(*args):
        return args[0] * args[1]
    def perimeter(*args):
        return 2 * (args[0] + args[1])

    lenght = args[0]
    width = args[1]
    if isinstance(lenght, int) and isinstance(width, int):
        return f"Rectangle area: {area(args[0], args[1])}\nRectangle perimeter: {perimeter(args[0], args[1])}"

    else:
        return "Enter valid values!"


print(rectangle(2, 10))
