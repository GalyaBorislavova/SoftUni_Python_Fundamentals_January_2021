legendary_items = {"shards": "Shadowmourne", "fragments": "Valanyr", "motes": "Dragonwrath"}
key_materials = {"shards": 0, "fragments": 0, "motes": 0}
junk = {}
win_legendary_item = False

while True:
    if win_legendary_item:
        break
    data = input().split()
    for i in range(0, len(data), 2):
        quantity = int(data[i])
        material = data[i + 1].lower()
        if material in key_materials:
            key_materials[material] += quantity
            for material, quantity in key_materials.items():
                if quantity >= 250:
                    win_legendary_item = True
                    print(f"{legendary_items[material]} obtained!")
                    key_materials[material] -= 250
        else:
            if material in junk:
                junk[material] += quantity
            else:
                junk[material] = quantity
        if win_legendary_item:
            break

for material, quantity in sorted(key_materials.items(), key=lambda x: (-x[1], x[0])):
    print(f"{material}: {quantity}")
for material, quantity in sorted(junk.items(), key=lambda x: (x[0])):
    print(f"{material}: {quantity}")