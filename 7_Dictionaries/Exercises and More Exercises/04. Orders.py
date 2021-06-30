data = input().split()
orders = {}

while "buy" not in data:
    product = data[0]
    price = float(data[1])
    quantity = int(data[2])
    if product not in orders:
        orders[product] = [price, quantity]
    else:
        old_price = orders[product][0]
        if old_price != price:
            orders[product][0] = price
        orders[product][1] += quantity

    data = input().split()

for product, price_quantity in orders.items():
    total_price = orders[product][0] * orders[product][1]
    print(f"{product} -> {total_price:.2f}")