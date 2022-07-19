num_computers = int(input())
sales_done = 0
total_rating = 0
for i in range(num_computers):
    rating_sales = int(input())
    rating = rating_sales % 10
    total_rating += rating
    sales = int(str(rating_sales)[:2])
    if rating == 2:
        continue
    if rating == 3:
        sales_done += sales * 0.50
    if rating == 4:
        sales_done += sales * 0.70
    if rating == 5:
        sales_done += sales * 0.85
    if rating == 6:
        sales_done += sales
average_rating = total_rating / num_computers
print(f'{sales_done:.2f}')
print(f'{average_rating:.2f}')
