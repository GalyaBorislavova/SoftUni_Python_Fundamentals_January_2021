number_of_lost_fights = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

expenses = 0
count = 0

for lost in range(1, number_of_lost_fights + 1):
    if lost % 2 == 0 and lost % 3 == 0:
        expenses += (helmet_price + sword_price + shield_price)
        count += 1
        if count % 2 == 0:
            expenses += armor_price
    elif lost % 2 == 0:
        expenses += helmet_price
    elif lost % 3 == 0:
        expenses += sword_price

print(f"Gladiator expenses: {expenses:.2f} aureus")