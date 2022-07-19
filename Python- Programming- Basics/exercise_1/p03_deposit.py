deposit_sum = float(input())
months = int(input())
year_gain_percent = float(input()) / 100

monthly_gain = (deposit_sum * year_gain_percent) / 12
deposit_sum_gain = (monthly_gain * months) + deposit_sum
print(deposit_sum_gain)