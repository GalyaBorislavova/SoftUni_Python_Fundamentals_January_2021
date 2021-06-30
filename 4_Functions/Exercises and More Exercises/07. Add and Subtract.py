n1 = int(input())
n2 = int(input())
n3 = int(input())


def sum_numbers(num1, num2):
    return num1 + num2


def subtract_numbers(s, num3):
    return s - num3


def add_and_subtract(num1, num2, num3):
    result = sum_numbers(num1, num2)
    return subtract_numbers(result, num3)


print(add_and_subtract(n1, n2, n3))