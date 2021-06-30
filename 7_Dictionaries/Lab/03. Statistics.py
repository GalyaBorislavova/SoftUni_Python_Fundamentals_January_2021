data = input()
statistics = {}

while not data == "statistics":
    product, quantity = data.split(": ")
    if product not in statistics:
        statistics[product] = int(quantity)
    else:
        statistics[product] += int(quantity)
    data = input()

print("Products in stock:")

for product, quantity in statistics.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(statistics)}")
print(f"Total Quantity: {sum(statistics.values())}")