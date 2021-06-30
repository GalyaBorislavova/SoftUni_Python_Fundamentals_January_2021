number_of_commands = int(input())
parking = {}

for n in range(number_of_commands):
    command = input().split()
    register_or_unregister = command[0]
    username = command[1]
    if register_or_unregister == "register":
        license_plate_number = command[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {license_plate_number}")
        else:
            parking[username] = license_plate_number
            print(f"{username} registered {license_plate_number} successfully")
    elif register_or_unregister == "unregister":
        if username in parking:
            del parking[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for name, plate_number in parking.items():
    print(f"{name} => {plate_number}")