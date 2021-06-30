number_of_wagons = int(input())
wagons = [0] * number_of_wagons

command = input()
while not command == "End":
    data = command.split()
    action = data[0]
    if action == "add":
        people = int(data[1])
        wagons[-1] += people
    elif action == "insert":
        index = int(data[1])
        people = int(data[2])
        wagons[index] += people
    elif action == "leave":
        index = int(data[1])
        people = int(data[2])
        wagons[index] -= people

    command = input()

print(wagons)