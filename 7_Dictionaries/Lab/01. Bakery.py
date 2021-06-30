data = input().split()
bakery = {}

for index in range(0, len(data), 2):
    product = data[index]
    quantity = int(data[index + 1])
    bakery[product] = quantity

print(bakery)
