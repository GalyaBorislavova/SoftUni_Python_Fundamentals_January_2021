inventory = input().split(", ")
command = input().split(" - ")

while "Craft!" not in command:
    if "Collect" in command:
        item = command[1]
        if item not in inventory:
            inventory.append(item)
    elif "Drop" in command:
        item = command[1]
        if item in inventory:
            inventory.remove(item)
    elif "Combine Items" in command:
        command_data = command[1].split(":")
        old_item = command_data[0]
        new_item = command_data[1]
        if old_item in inventory:
           index_old_item = inventory.index(old_item)
           inventory.insert(index_old_item + 1, new_item)
    elif "Renew" in command:
        item = command[1]
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)
    command = input().split(" - ")

print(*inventory, sep=", ")