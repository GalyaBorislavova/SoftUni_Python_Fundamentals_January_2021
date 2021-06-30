command = input()

number_of_coffee = 0
events = ["coding", "dog", "cat", "movie"]
events_upper = [word.upper() for word in events]

while not command == "END":
    if command in events:
        number_of_coffee += 1
    elif command in events_upper:
        number_of_coffee += 2
    if number_of_coffee > 5:
        print("You need extra sleep")
        break
    command = input()

else:
    print(number_of_coffee)
