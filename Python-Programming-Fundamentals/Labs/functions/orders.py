def calculation(type_product, quantity):
    if type_product == 'coffee':
        return quantity * 1.50
    elif type_product == 'water':
        return quantity * 1
    elif type_product == 'coke':
        return quantity * 1.40
    elif type_product == 'snacks':
        return quantity * 2


product = input()
product_quantity = int(input())
print(f'{calculation(product, product_quantity):.2f}')