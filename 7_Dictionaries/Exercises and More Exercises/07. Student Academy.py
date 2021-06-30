number_of_rows = int(input())
student_diary = {}

for n in range(number_of_rows):
    name_of_student = input()
    grade = float(input())
    if name_of_student in student_diary:
        student_diary[name_of_student].append(grade)
    else:
        student_diary[name_of_student] = [grade]

average_grades = {k: sum(v) / len(v) for k, v in student_diary.items() if sum(v) / len(v) >= 4.5}
for student, grade in sorted(average_grades.items(), key=lambda x: -x[1]):
    print(f"{student} -> {grade:.2f}")
