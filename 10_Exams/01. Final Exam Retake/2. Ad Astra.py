import re

data = input()
pattern = r"(#|\|)(?P<name>[A-Za-z\s]+)\1(?P<expiration>\d{2}/\d{2}/\d{2})\1(?P<calories>[0-9]{1,4}|10000)\1"
products = [match_obj.groupdict() for match_obj in re.finditer(pattern, data)]
total_calories = sum([int(product['calories']) for product in products])
print(f"You have food to last you for: {total_calories // 2000} days!")
for product in products:
    print(f"Item: {product['name']}, Best before: {product['expiration']}, Nutrition: {product['calories']}")