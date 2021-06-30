message = input()
data = input()

while not data == "Reveal":
    flag = False
    data = data.split(":|:")
    command = data[0]
    if command == "InsertSpace":
        index = int(data[1])
        message = message[:index] + " " + message[index:]
    elif command == "Reverse":
        substring = data[1]
        if substring in message:
            message = message.replace(substring, "", 1)
            reversed_substring = substring[::-1]
            message = message + reversed_substring
        else:
            flag = True
            print("error")
    elif command == "ChangeAll":
        substring = data[1]
        replacement = data[2]
        message = message.replace(substring, replacement)
    if not flag:
        print(message)
    data = input()


print(f"You have a new text message: {message}")