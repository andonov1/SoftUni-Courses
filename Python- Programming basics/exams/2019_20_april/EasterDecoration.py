num_clients = int(input())
sales_cnt = 0
total_sales = 0
for num in range(num_clients):
    type_product = input()
    curr_cnt = 0
    curr_sales = 0
    while True:
        if type_product == 'Finish':
            if curr_cnt % 2 == 0:
                curr_sales -= curr_sales * 0.20
                total_sales += curr_sales
            else:
                total_sales += curr_sales
            sales_cnt += 1
            print(f"You purchased {curr_cnt} items for {curr_sales:.2f} leva.")
            break
        elif type_product == 'basket':
            curr_sales += 1.50
            curr_cnt += 1
        elif type_product == 'wreath':
            curr_sales += 3.80
            curr_cnt += 1
        elif type_product == 'chocolate bunny':
            curr_sales += 7
            curr_cnt += 1
        type_product = input()
average_bill = total_sales / sales_cnt
print(f"Average bill per client is: {average_bill:.2f} leva.")




