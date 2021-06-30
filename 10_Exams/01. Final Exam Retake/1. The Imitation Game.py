encrypted_message = input()
command = input()

while not command == "Decode":
    command = command.split("|")
    action = command[0]
    if action == "Move":
        n = int(command[1])
        chars_to_back = encrypted_message[:n]
        encrypted_message = encrypted_message[n:] + chars_to_back
    elif action == "Insert":
        index = int(command[1])
        value = command[2]
        encrypted_message = encrypted_message[:index] + value + encrypted_message[index:]
    elif action == "ChangeAll":
        substring = command[1]
        replacement = command[2]
        encrypted_message = encrypted_message.replace(substring, replacement)
    command = input()
print(f"The decrypted message is: {encrypted_message}")