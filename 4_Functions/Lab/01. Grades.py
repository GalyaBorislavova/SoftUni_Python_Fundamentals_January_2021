grade = float(input())


def grade_as_string(student_grade):
    if 2.00 <= student_grade <= 2.99:
        return "Fail"
    elif 3.00 <= student_grade <= 3.49:
        return "Poor"
    elif 3.50 <= student_grade <= 4.49:
        return "Good"
    elif 4.50 <= student_grade <= 5.49:
        return "Very Good"
    elif 5.50 <= student_grade <= 6.00:
        return "Excellent"


print(grade_as_string(grade))
