divisor = int(input())
bound = int(input())
isFound = False
biggest_number = 0

for number in range(1, bound + 1):
    if number % divisor == 0:
        isFound = True
        if number > biggest_number:
            biggest_number = number

print(biggest_number)