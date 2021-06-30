import re

text = input()
searched_word = input()
pattern = rf"{searched_word}\b"
match = re.findall(pattern, text, re.IGNORECASE)
print(len(match))