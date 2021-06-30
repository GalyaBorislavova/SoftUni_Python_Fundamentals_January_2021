age = int(input())
current_drink = ""

if 0 < age <= 14:
    current_drink = "toddy"
elif age <= 18:
    current_drink = "coke"
elif age <= 21:
    current_drink = "beer"
else:
    current_drink = "whisky"

print(f"drink {current_drink}")
