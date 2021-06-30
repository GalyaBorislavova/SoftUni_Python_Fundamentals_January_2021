text = input()
encrypted_text = ""

for index in range(0, len(text)):
    encrypted_text += chr((ord(text[index])) + 3)
print(encrypted_text)