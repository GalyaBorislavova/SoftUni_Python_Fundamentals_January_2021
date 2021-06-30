list_of_gifts = input().split()
command = input().split()
command_as_string = " ".join(command)
new_list = ""

while "No Money" not in command_as_string:
    current_gift = command[1]
    if "OutOfStock" in command:
        if current_gift in list_of_gifts:
            c = list_of_gifts.count(current_gift)
            for i in range(c):
                count_gifts = list_of_gifts.index(current_gift)
                list_of_gifts[count_gifts] = "None"
    elif "Required" in command:
        current_index = int(command[2])
        if 0 <= current_index < len(list_of_gifts):
            list_of_gifts.insert(current_index, current_gift)
            list_of_gifts.pop(current_index + 1)
    elif "JustInCase" in command:
        list_of_gifts.pop(-1)
        list_of_gifts.append(current_gift)

    command = input().split()
    command_as_string = " ".join(command)

count_none = list_of_gifts.count("None")
for none in range(count_none):
    list_of_gifts.remove("None")

new_list = " ".join(list_of_gifts)
print(new_list)
