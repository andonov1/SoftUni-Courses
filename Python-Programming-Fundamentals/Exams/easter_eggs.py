import re

text = input()
pattern = r'[@|#]+(?P<color>[a-z]{3,})[@|#]+(?P<separator>[^A-Za-z0-9]+)?[/]+(?P<amount>\d+)[/]+'

for match in re.finditer(pattern, text):
    print(f"You found {match.groupdict()['amount']} {match.groupdict()['color']} eggs!")