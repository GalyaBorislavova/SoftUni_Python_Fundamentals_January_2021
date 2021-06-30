cities = {}
command = input()
while not command == "Sail":
    data = command.split("||")
    city = data[0]
    population, gold = [int(i) for i in data[1:]]
    if city not in cities:
        cities[city] = {"Population": population, "Gold": gold}
    else:
        cities[city]["Population"] += population
        cities[city]["Gold"] += gold
    command = input()
command = input()
while not command == "End":
    data = command.split("=>")
    action = data[0]
    city = data[1]
    if action == "Plunder":
        people, gold = [int(i) for i in data[2:]]
        if city in cities:
            cities[city]["Population"] -= people
            cities[city]["Gold"] -= gold
        print(f"{city} plundered! {gold} gold stolen, {people} citizens killed.")
        if cities[city]["Gold"] <= 0 or cities[city]["Population"] <= 0:
            del cities[city]
            print(f"{city} has been wiped off the map!")
    elif action == "Prosper":
        gold = int(data[2])
        if gold > 0:
            if city in cities:
                cities[city]["Gold"] += gold
            print(f"{gold} gold added to the city treasury. {city} now has {cities[city]['Gold']} gold.")
        else:
            print("Gold added cannot be a negative number!")
    command = input()

if not cities:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")
else:
    print(f"Ahoy, Captain! There are {len(cities)} wealthy settlements to go to:")
    for city, population_gold in sorted(cities.items(), key=lambda x: (-x[1]['Gold'], x[0])):
        print(f"{city} -> Population: {population_gold['Population']} citizens, Gold: {population_gold['Gold']} kg")

