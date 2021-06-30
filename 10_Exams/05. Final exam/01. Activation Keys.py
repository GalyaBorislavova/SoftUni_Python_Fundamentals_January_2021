raw_activation_key = input()
data = input()
while not data == "Generate":
    data = data.split(">>>")
    command = data[0]
    if command == "Contains":
        substring = data[1]
        if substring in raw_activation_key:
            print(f"{raw_activation_key} contains {substring}")
        else:
            print("Substring not found!")
    elif command == "Flip":
        upper_or_lower = data[1]
        start_index = int(data[2])
        end_index = int(data[3])
        substring = raw_activation_key[start_index:end_index]
        if upper_or_lower == "Lower":
            substring = substring.lower()
            raw_activation_key = raw_activation_key[:start_index] + substring + raw_activation_key[end_index:]
        elif upper_or_lower == "Upper":
            substring = substring.upper()
            raw_activation_key = raw_activation_key[:start_index] + substring + raw_activation_key[end_index:]
        print(raw_activation_key)
    elif command == "Slice":
        start_index, end_index = [int(ind) for ind in data[1:]]
        raw_activation_key = raw_activation_key[:start_index] + raw_activation_key[end_index:]
        print(raw_activation_key)

    data = input()
print(f"Your activation key is: {raw_activation_key}")