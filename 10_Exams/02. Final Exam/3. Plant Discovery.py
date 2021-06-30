n = int(input())
plants = {}

for _ in range(n):
    plant_name, rarity = input().split("<->")
    plants[plant_name] = {"rarity": int(rarity), "rating": []}
command = input()

while not command == "Exhibition":
    action, data = command.split(": ")
    try:
        if action == "Rate":
            plant, rating = data.split(" - ")
            plants[plant]["rating"].append(int(rating))
        elif action == "Update":
            plant, new_rarity = data.split(" - ")
            plants[plant]["rarity"] = int(new_rarity)
        elif action == "Reset":
            plant = data
            plants[plant]["rating"].clear()
        else:
            print("error")
    except KeyError:
        print("error")
    command = input()

for key, values in plants.items():
    if values["rating"]:
        average = sum(values['rating']) / len(values["rating"])
    else:
        average = 0
    plants[key]["avg"] = average

print("Plants for the exhibition:")
for plant, data_value in sorted(plants.items(), key=lambda x: (-x[1]['rarity'], -x[1]['avg'])):
    print(f"- {plant}; Rarity: {data_value['rarity']}; Rating: {data_value['avg']:.2f}")