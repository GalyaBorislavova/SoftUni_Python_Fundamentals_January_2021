n = int(input())

for num in range(1, n + 1):
    sum_digit = 0
    for index_digit in str(num):
        sum_digit += int(index_digit)
    if sum_digit == 5 or sum_digit == 7 or sum_digit == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")