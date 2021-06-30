single_number = input()


def sum_even_and_odd(number_string):
    sum_even = 0
    sum_odd = 0
    for digits in number_string:
        if int(digits) % 2 == 0:
            sum_even += int(digits)
        else:
            sum_odd += int(digits)
    print(f"Odd sum = {sum_odd}, Even sum = {sum_even}")


sum_even_and_odd(single_number)