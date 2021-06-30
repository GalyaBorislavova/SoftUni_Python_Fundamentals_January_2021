number = input()

length = len(number)
largest_number = ""
index = 0

digits_list = list(number)
digits_list.sort(reverse=True)

for i in range(length):
    digit = digits_list[index]
    largest_number += digit
    index += 1

print(largest_number)