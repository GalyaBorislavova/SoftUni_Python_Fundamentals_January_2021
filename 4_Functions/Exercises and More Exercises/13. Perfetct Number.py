def print_perfect_number_or_not(num):
    sum_numbers = 0
    if num > 0:
        for divider in range(1, num):
            if num % divider == 0:
                sum_numbers += divider
        if sum_numbers == num:
            print("We have a perfect number!")
        else:
            print("It's not so perfect.")


number = int(input())
print_perfect_number_or_not(number)