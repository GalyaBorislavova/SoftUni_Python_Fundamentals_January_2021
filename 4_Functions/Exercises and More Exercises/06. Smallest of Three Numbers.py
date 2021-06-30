num1 = int(input())
num2 = int(input())
num3 = int(input())


def smallest(number1, number2, number3):
    smallest_number = min(number1, number2, number3)
    return smallest_number
    # if number1 < number2 and number1 < number3:
    #     result = number1
    # elif number2 < number1 and number2 < number3:
    #     result = number2
    # elif number3 < number2 and number3 < number1:
    #     result = number3
    # elif number1 == number2 or number1 == number3:
    #     result = number1
    # else:
    #     result = number2
    # return result


print(smallest(num1, num2, num3))