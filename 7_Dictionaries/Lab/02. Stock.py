data = input().split()
searched_products = input().split()
stock = {}

for index in range(0, len(data), 2):
    product = data[index]
    quantity = data[index + 1]
    stock[product] = int(quantity)

for searched_product in searched_products:
    if searched_product not in stock:
        print(f"Sorry, we don't have {searched_product}")
    else:
        print(f"We have {stock[searched_product]} of {searched_product} left")