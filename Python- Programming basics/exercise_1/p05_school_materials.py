number_pensils = int(input())
number_markers = int(input())
litre_cleaning_fluid = int(input())
discount = float(input()) / 100

pensils_price = number_pensils * 5.80
markers_price = number_markers * 7.20
cleaning_fluid_price = litre_cleaning_fluid * 1.20

total_discount = (pensils_price + markers_price + cleaning_fluid_price) * discount
total_price_with_discount = (pensils_price + markers_price +cleaning_fluid_price) - total_discount
print(total_price_with_discount)

