people = {p:0 for p in input().split(", ")}
command = input()
while not command == "end of race":
    name = ""
    distance = 0
    for char in command:
        if char.isalpha():
            name += char
        elif char.isdigit():
            distance += int(char)
    if name in people:
        people[name] += distance
    command = input()
winners = sorted(people.items(), key=lambda x: -x[1])
print(f"1st place: {winners[0][0]}")
print(f"2nd place: {winners[1][0]}")
print(f"3rd place: {winners[2][0]}")