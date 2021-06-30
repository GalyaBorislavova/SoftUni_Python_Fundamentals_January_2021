cars = {}
n = int(input())
for _ in range(n):
    data_current_car = input()
    data_current_car = data_current_car.split("|")
    car_name = data_current_car[0]
    mileage, fuel = [int(i) for i in data_current_car[1:]]
    cars[car_name] = {"Mileage": mileage, "Fuel": fuel}

command = input()

while not command == "Stop":
    command = command.split(" : ")
    action = command[0]
    car_name = command[1]
    if action == "Drive":
        distance = int(command[2])
        fuel = int(command[3])
        if cars[car_name]['Fuel'] > fuel:
            cars[car_name]["Mileage"] += distance
            cars[car_name]["Fuel"] -= fuel
            print(f"{car_name} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
        else:
            print("Not enough fuel to make that ride")
        if cars[car_name]["Mileage"] >= 100000:
            del cars[car_name]
            print(f"Time to sell the {car_name}!")
    elif action == "Refuel":
        fuel = int(command[2])
        if cars[car_name]["Fuel"] + fuel <= 75:
            cars[car_name]["Fuel"] = cars[car_name]["Fuel"] + fuel
            print(f"{car_name} refueled with {fuel} liters")
        else:
            print(f"{car_name} refueled with {75 - cars[car_name]['Fuel']} liters")
            cars[car_name]["Fuel"] = 75
    elif action == "Revert":
        kilometers = int(command[2])
        cars[car_name]["Mileage"] -= kilometers
        if cars[car_name]["Mileage"] < 10000:
            cars[car_name]["Mileage"] = 10000
        else:
            print(f"{car_name} mileage decreased by {kilometers} kilometers")
    command = input()

for car, m_f in sorted(cars.items(),key=lambda x: (-x[1]['Mileage'], x[0])):
    print(f"{car} -> Mileage: {m_f['Mileage']} kms, Fuel in the tank: {m_f['Fuel']} lt.")