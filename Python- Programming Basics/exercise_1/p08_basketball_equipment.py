subscription_tax = int(input())

shoes = subscription_tax - subscription_tax * 0.40
clothes = shoes - shoes * 0.20
ball = clothes - clothes * 0.75
accessories = ball - ball * 0.80
total = subscription_tax + shoes + clothes + ball + accessories
print(total)