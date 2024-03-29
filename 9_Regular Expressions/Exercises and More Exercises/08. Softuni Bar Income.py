import re

pattern = r"%(?P<customer>[A-Z]{1}[a-z]+)%[^\|\$%\.]*\<(?P<product>\w+)>[^\|\$%\.]*\|(?P<count>\d+)\|([^\$%\.0-9]*|(?<=\|))(?P<price>[0-9]+(\.)?([0-9]+)?)\$"
data = input()
total_income = 0
while not data == "end of shift":
    order = [p.groupdict() for p in re.finditer(pattern, data)]
    if order:
        count = int(order[0]['count'])
        price = float(order[0]['price'])
        total_price = count * price
        total_income += total_price
        print(f"{order[0]['customer']}: {order[0]['product']} - {total_price:.2f}")
    data = input()
print(f"Total income: {total_income:.2f}")