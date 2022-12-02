import re

n = int(input())
pattern = r'@#{1,}(?P<item>[A-Z][A-Za-z\d]{4,}[A-Z])@#{1,}'
pattern_2 = r'\d'

for i in range(n):
    text = input()
    if re.search(pattern, text):
        for match in re.finditer(pattern, text):
            if match.group():
                digits = re.findall(pattern_2, match.group())
                if digits:
                    group = ''
                    for digit in digits:
                        group += digit
                else:
                    group = "00"
                print(f'Product group: {group}')
    else:
        print("Invalid barcode")
