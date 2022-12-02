import re

text = input()
locations = []
pattern = r'(?P<separator>=|/)(?P<destination>[A-Z][A-z]{2,})(?P=separator)'
travel_points = 0

for match in re.finditer(pattern, text):
    locations.append(match.groupdict()['destination'])

for location in locations:
    travel_points += len(location)

print(f"Destinations: {', '.join(locations)}")
print(f"Travel Points: {travel_points}")