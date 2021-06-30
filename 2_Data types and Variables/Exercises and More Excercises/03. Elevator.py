import math

number_of_people = int(input())
capacity_elevator = int(input())

number_of_full_courses = 0
count = 0

if number_of_people % capacity_elevator == 0:
    count = number_of_people // capacity_elevator
else:
    count = math.ceil(number_of_people / capacity_elevator)
print(count)

