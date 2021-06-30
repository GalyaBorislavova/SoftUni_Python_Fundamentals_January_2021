number_of_rooms = int(input())
room = [(input()).split(" ") for r in range(number_of_rooms)]
if sum([room[i][0].count("X") for i in range(number_of_rooms)]) < sum([int(room[sub][-1])for sub in range(len(room))]):
    for r in range(number_of_rooms):
        current_room = room[r]
        people = int(room[r][-1])
        chairs = room[r][0].count("X")
        if chairs < people:
            print(f"{people - chairs} more chairs needed in room {r + 1}")
else:
    left_chairs = [int(room[x][0].count("X") - int(room[x][-1])) for x in range(number_of_rooms) if room[x][0].count("X") > int(room[x][-1])]
    print(f"Game On, {sum(left_chairs)} free chairs left")