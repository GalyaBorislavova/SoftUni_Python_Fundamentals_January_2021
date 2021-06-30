items = input().split("|")
budget = float(input())

sum_of_buy = []
profit = 0
spend_money = 0

for item in items:
    item = item.split("->")
    item_type = item[0]
    price = float(item[1])
    if item_type == "Clothes":
        if price > 50:
            continue
    elif item_type == "Shoes":
        if price > 35:
            continue
    elif item_type == "Accessories":
        if price > 20.50:
            continue
    if budget >= price:
        budget -= price
        spend_money += price
        new_price = price * 1.4
        profit += new_price
        sum_of_buy.append(new_price)

for x in range(len(sum_of_buy)):
    print(f"{sum_of_buy[x]:.2f}", end=" ")
print("")

print(f"Profit: {abs(profit - spend_money):.2f}")
if (profit + budget) >= 150:
    print("Hello, France!")
else:
    print("Time to go.")
