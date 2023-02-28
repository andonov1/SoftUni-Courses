def shopping_cart(*args):
    meals = {'Soup': [],
             'Pizza': [],
             'Dessert': []}
    limits = {'Soup': 3,
              'Pizza': 4,
              'Dessert': 2}
    result = ''
    no_product = True

    for el in args:
        if el == 'Stop':
            break
        meal, product = el[0], el[1]
        if limits[meal] > 0:
            no_product = False
            if product not in meals[meal]:
                meals[meal].append(product)
                limits[meal] -= 1

    if no_product:
        result += f"No products in the cart!"

    else:
        sorted_meals = sorted(meals.items(), key=lambda x: (-len(x[1]), x[0]))

        for meal_tuple in sorted_meals:
            result += f'{meal_tuple[0]}:\n'
            for product in sorted(meal_tuple[1]):
                result += f' - {product}\n'

    return result


print(shopping_cart(
    'Stop',
    ('Pizza', 'ham'),
    ('Pizza', 'mushrooms'),
))
