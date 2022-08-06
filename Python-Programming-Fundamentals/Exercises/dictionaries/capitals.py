countries = input().split(", ")
capitals = input().split(", ")
result = {countries[i]: capitals[i] for i in range(len(capitals))}

for country, capital in result.items():
    print(f"{country} -> {capital}")