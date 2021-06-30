operator = input()
num1 = int(input())
num2 = int(input())


def calculator(n1, n2, sign):
    if sign == "add":
        return n1 + n2
    elif sign == "subtract":
        return n1 - n2
    elif sign == "divide":
        return n1 // n2
    else:
        return n1 * n2


print(calculator(num1, num2, operator))