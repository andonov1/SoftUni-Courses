import re

text = input()
threshold = 1
emoji_cnt = 0
cool_emojis = []
pattern_1 = r'\d'
pattern_2 = r'(?P<separator>\:\:|\*\*)(?P<emoji>[A-Z][a-z]{2,})(?P=separator)'

for match in re.findall(pattern_1, text):
    threshold *= int(match)
print(f"Cool threshold: {threshold}")

for match in re.finditer(pattern_2, text):
    current_coolness = 0
    emoji_cnt += 1
    data = match.groupdict()
    emoji = data['emoji']
    for char in emoji:
        current_coolness += ord(char)
    if current_coolness >= threshold:
        cool_emojis.append(match.group())

print(f"{emoji_cnt} emojis found in the text. The cool ones are:")
for emoji in cool_emojis:
    print(emoji)

