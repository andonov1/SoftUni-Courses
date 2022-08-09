text = input()
encrypted_text = ''
for i in text:
    encrypted_text += chr(ord(i) + 3)

print(encrypted_text)