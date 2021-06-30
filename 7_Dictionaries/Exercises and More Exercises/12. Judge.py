result = {}
students = {}

data = input()

while not data == "no more time":
    username, contest, points = data.split(" -> ")
    points = int(points)

    if contest not in result:
        result[contest] = {}

    if username not in result[contest]:
        result[contest][username] = points
    else:
        if result[contest][username] < points:
            result[contest][username] = points
            students[username] = points
        data = input()
        continue

    if username not in students:
        students[username] = points
    else:
        students[username] += points

    data = input()

for contest, student_data in result.items():
    print(f"{contest}: {len(result[contest])} participants")
    sorted_students = dict(sorted(student_data.items(), key=lambda x: (-x[1], x[0])))
    for ind, student_grade in enumerate(sorted_students.items()):
        print(f"{ind + 1}. {student_grade[0]} <::> {student_grade[1]}")

print("Individual standings:")

sorted_grades = dict(sorted(students.items(), key=lambda x: (-x[1], x[0])))
for ind, student_grades in enumerate(sorted_grades.items()):
    print(f"{ind + 1}. {student_grades[0]} -> {student_grades[1]}")
