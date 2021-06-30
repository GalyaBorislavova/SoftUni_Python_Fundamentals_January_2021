data = input()

for index in range(0, len(data)):
    if data[index] == data[index + 1]:
        while data[index] == data[index + 1] and index + 1 in range(0, len(data)):
            double = f"{data[index]}{data[index + 1]}"
            to_replace = f"{data[index]}"
            data = data.replace(double, to_replace)
            index = index
            if index + 1 not in range(0, len(data)):
                break
    else:
        if index + 1 in range(0, len(data)):
            index += 1
        else:
            break
    if index + 2 not in range(0, len(data)):
        break

print(data)
