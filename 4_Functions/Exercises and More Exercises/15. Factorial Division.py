import math


def calculate_factorial(number):
    return math.factorial(number)


def divide_two_factorials(f1, f2):
    return f1 / f2


num1 = int(input())
num2 = int(input())
factorial_num1 = calculate_factorial(num1)
factorial_num2 = calculate_factorial(num2)
result = divide_two_factorials(factorial_num1, factorial_num2)
print(f"{result:.2f}")