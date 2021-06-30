first_symbol = input()
second_symbol = input()
text = input()
ascii_sum = 0
max_ascii = max(ord(first_symbol), ord(second_symbol))
min_ascii = min(ord(first_symbol), ord(second_symbol))

for l in text:
    if min_ascii < ord(l) < max_ascii:
        ascii_sum += ord(l)

print(ascii_sum)

