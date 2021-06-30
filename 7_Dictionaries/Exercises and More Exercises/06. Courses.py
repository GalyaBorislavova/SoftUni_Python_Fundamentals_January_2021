command = input().split(" : ")
courses = {}

while "end" not in command:
    name_of_course = command[0]
    name_of_student = command[1]
    if name_of_course not in courses:
        courses[name_of_course] = [name_of_student]
    else:
        courses[name_of_course].append(name_of_student)
    command = input().split(" : ")

for course, people in sorted(courses.items(), key=lambda x: -len(x[1])):
    print(f"{course}: {len(courses[course])}")
    for name in sorted(courses[course]):
        print(f"-- {name}")

