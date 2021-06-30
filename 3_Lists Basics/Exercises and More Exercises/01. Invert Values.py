string_of_numbers = input()
numbers = string_of_numbers.split(" ")
invert = []

for elements in numbers:
    invert_digit = - int(elements)
    invert.append(invert_digit)


print(invert)
