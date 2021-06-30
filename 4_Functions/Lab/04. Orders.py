product = input()
n = int(input())


def shop(prod, count, price=0):
    if prod == "coffee":
        price = 1.5
    elif prod == "water":
        price = 1
    elif prod == "coke":
        price = 1.4
    elif prod == "snacks":
        price = 2
    total = price * count

    return total


print(f"{shop(product, n):.2f}")

