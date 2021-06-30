import re

pattern = r">>(?P<name>[A-Za-z]+)<<(?P<price>\d+(\.)?(\d+)?)!(?P<quantity>\d+)"
spend_money = 0
command = input()
furniture_names = []
while not command == "Purchase":
    match = re.match(pattern, command)
    if match:
        data = match.groupdict()
        furniture_names.append(data["name"])
        price = float(data["price"])
        quantity = int(data["quantity"])
        spend_money += (price * quantity)
    command = input()

print("Bought furniture:")
for f in furniture_names:
    print(f"{f}")
print(f"Total money spend: {spend_money:.2f}")