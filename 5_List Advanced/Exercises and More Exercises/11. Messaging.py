numbers_list = input().split()
text = [x for x in input()]

my_text = ""
count = 0
index = 0

for num in numbers_list:
    current_sum = 0
    for digit in num:
        current_sum += int(digit)
    if current_sum <= len(text) - 1:
        my_text += text[current_sum]
        text.remove(text[current_sum])
    else:
        while count <= len(text) - 1:
            index += 1
            count += 1
            if len(text) - 1 == index:
                index = 0
        else:
            my_text += text[index]
            text.remove(text[index])

print(my_text)

