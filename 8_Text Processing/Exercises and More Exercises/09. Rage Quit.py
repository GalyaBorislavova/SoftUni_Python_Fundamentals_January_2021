data = input()
result = ""
current_part = ""

for index, el in enumerate(data):
    digit = ""
    if el.isdigit():
        digit += el
        while el.isdigit and index + 1 in range(0, len(data)):
            if data[index + 1].isdigit():
                digit += data[index + 1]
                index += 1
            else:
                break
        result += current_part.upper() * int(digit)
        current_part = ""
    else:
        current_part += el

set_of_elements = set(result)
print(f"Unique symbols used: {len(set_of_elements)}")
print(result)
