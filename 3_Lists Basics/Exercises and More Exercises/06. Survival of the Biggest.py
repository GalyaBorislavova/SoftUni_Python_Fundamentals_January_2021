numbers = input().split() # as a string
amount_of_numbers_to_remove = int(input())

for i in range(0, len(numbers)):
    numbers[i] = int(numbers[i])

min_element = 0
for removes in range(amount_of_numbers_to_remove):
    min_element = min(numbers)
    numbers.remove(min_element)


print(numbers)