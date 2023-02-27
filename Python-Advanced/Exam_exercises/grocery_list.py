def shop_from_grocery_list(budget, grocery_list=[], *args):
    cart = []
    result = ''

    for product, price in args:
        price = float(price)
        if budget < price:
            break
        if product in grocery_list and product not in cart:
            cart.append(product)
            budget -= price

    if len(grocery_list) == len(cart):
        result += f"Shopping is successful. Remaining budget: {budget:.2f}."
    else:
        missing_products = []
        for product in grocery_list:
            if product not in cart:
                missing_products.append(product)
        result += f"You did not buy all the products. Missing products: {', '.join(s for s in missing_products)}."
    return result


print(shop_from_grocery_list(
    100,
    ["tomato", "cola", "chips", "meat"],
    ("cola", 5.8),
    ("tomato", 10.0),
    ("meat", 22),
))
