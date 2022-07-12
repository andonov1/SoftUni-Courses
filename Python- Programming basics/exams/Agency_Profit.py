name_airline = input()
adult_tickets = int(input())
kids_tickets = int(input())
adult_ticket_price = float(input())
tax = float(input())
price_adult_tax = adult_ticket_price + tax
kids_tickets_price = adult_ticket_price * 0.30 + tax
total_ticket = adult_tickets + kids_tickets
total_sales = (adult_tickets * price_adult_tax) + (kids_tickets * kids_tickets_price)
revenue = total_sales * 0.20

print(f"The profit of your agency from {name_airline} tickets is {revenue:.2f} lv.")
