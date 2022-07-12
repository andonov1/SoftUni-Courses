bitcoins = int(input())
chinese_yoan = float(input())
commission = float(input()) / 100

total_leva = 0

amount_btc_leva = bitcoins * 1168
chinese_yoan_leva = (chinese_yoan * 0.15) * 1.76
total_euro = (amount_btc_leva + chinese_yoan_leva) / 1.95
total_euro_withhold_commission = total_euro - (total_euro * commission)
print(f'{total_euro_withhold_commission:.2f}')

