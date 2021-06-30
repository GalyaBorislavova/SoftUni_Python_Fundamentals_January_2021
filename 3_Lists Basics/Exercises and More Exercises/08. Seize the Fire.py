cells_list = input().split("#") # High = 89#Low = 28#Medium = 77#Low = 23
water = int(input())

total_effort = 0
total_fire = 0
cells = []

for el in cells_list:
    el = el.split(" = ")
    current_value = int(el[1])
    current_type_fire = el[0]
    if current_type_fire == "High":
        if not 81 <= current_value <= 125:
            continue
    elif current_type_fire == "Medium":
        if not 51 <= current_value <= 80:
            continue
    elif current_type_fire == "Low":
        if not 1 <= current_value <= 50:
            continue
    if water < current_value:
        continue
    cells.append(current_value)
    water -= current_value
    total_effort += current_value * 0.25
    total_fire += current_value

print("Cells:")
for element in cells:
    print(f" - {element}")
print(f"Effort: {total_effort:.2f}")
print(f"Total Fire: {total_fire}")