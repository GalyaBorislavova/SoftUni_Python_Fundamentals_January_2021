def valid_index(ind, text):
    if 0 <= ind < len(text):
        return True
    return False


initial_string = input()
command = input()

while not command == "Travel":
    command, data_1, data_2 = command.split(":")
    if command.startswith("Add"):
        index = int(data_1)
        string = data_2
        if valid_index(index, initial_string):
            initial_string = initial_string[:index] + string + initial_string[index:]
    elif command.startswith("Remove"):
        start_index = int(data_1)
        end_index = int(data_2)
        if valid_index(start_index, initial_string) and valid_index(end_index, initial_string):
            part_to_remove = initial_string[start_index:end_index + 1]
            initial_string = initial_string[:start_index] + initial_string[end_index + 1:]
    elif command.startswith("Switch"):
        old_string = data_1
        new_string = data_2
        initial_string = initial_string.replace(old_string, new_string)
    print(initial_string)
    command = input()

print(f"Ready for world tour! Planned stops: {initial_string}")