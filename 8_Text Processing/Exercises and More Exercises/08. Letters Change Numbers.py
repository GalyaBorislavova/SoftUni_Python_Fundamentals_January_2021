lowercase = {chr(num + 97): num + 1 for num in range(0, 26)}
uppercase = {chr(num + 65): num + 1 for num in range(0, 26)}

data = [el.strip() for el in input().split()]
result = 0
for element in data:
    digit = ""
    current_result = 0
    first_letter = element[0]
    second_letter = element[-1]
    for char in element:
        if char.isdigit():
            digit += char
    if first_letter.isupper():
        letter_position = uppercase[first_letter]
        current_result = int(digit) / letter_position
    elif first_letter.islower():
        letter_position = lowercase[first_letter]
        current_result = int(digit) * letter_position
    if second_letter.isupper():
        position = uppercase[second_letter]
        current_result -= position
    elif second_letter.islower():
        position = lowercase[second_letter]
        current_result += position

    result += current_result


print(f"{result:.2f}")