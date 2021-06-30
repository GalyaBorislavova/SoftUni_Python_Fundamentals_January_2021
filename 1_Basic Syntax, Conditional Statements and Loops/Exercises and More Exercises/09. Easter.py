budget = float(input())
price_flour = float(input())  # for 1 kg
price_for_eggs = price_flour * 0.75  # 1
price_milk = price_flour * 1.25  # 1 liter or 4 breads

number_of_colored_eggs = 0
number_of_easter_breads = 0
spend_money = 0

price_for_products_for_one_easter_bread = price_flour + price_for_eggs + (price_milk / 4)
number_of_easter_breads += int(budget / price_for_products_for_one_easter_bread)
spend_money += price_for_products_for_one_easter_bread * number_of_easter_breads
for breads in range(1, number_of_easter_breads + 1):
    number_of_colored_eggs += 3
    if breads % 3 == 0:
        number_of_colored_eggs -= (breads - 2)

difference = abs(budget - spend_money)
print(
    f"You made {number_of_easter_breads} cozonacs! Now you have {number_of_colored_eggs} eggs and {difference:.2f}"
    f"BGN left.")
