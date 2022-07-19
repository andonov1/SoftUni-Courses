joinery_numb = int(input())
joinery_type = input()
# "90X130" или "100X150" или "130X180" или "200X300"
delivery_type = input()
# "With delivery",  "Without delivery"
price = 0

if joinery_type == "90X130":
    price = 110 * joinery_numb
    if 30 < joinery_numb <= 60:
        price *= 0.95
    elif joinery_numb > 60:
        price *= 0.92
elif joinery_type == "100X150":
    price = 140 * joinery_numb
    if 40 < joinery_numb <= 80:
        price *= 0.94
    elif joinery_numb > 80:
        price *= 0.9
elif joinery_type == "130X180":
    price = 190 * joinery_numb
    if 20 < joinery_numb <= 50:
        price *= 0.93
    elif joinery_numb > 50:
        price *= 0.88
elif joinery_type == "200X300":
    price = 250 * joinery_numb
    if 25 < joinery_numb <= 50:
        price *= 0.91
    elif joinery_numb > 50:
        price *= 0.86

if delivery_type == "With delivery":
    price += 60
if joinery_numb > 99:
    price *= 0.96
if joinery_numb < 10:
    print(f"Invalid order")
else:
    print(f"{price:.2f} BGN")