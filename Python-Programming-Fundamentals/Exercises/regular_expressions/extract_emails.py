import re
pattern = r'(?<=\s)(([a-z0-9]+[\-\.\_a-z0-9]*)@[a-z\-]+(\.[a-z]+)+)\b'
lines = input()
valid_emails = re.findall(pattern, lines)
for email in valid_emails:
    print(email[0])
