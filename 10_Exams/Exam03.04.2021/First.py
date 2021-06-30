email = input().strip()
command = input().strip()


while not command.startswith("Complete"):
    if command.startswith("Make Upper"):
        email = email.upper()
        print(email)
    elif command.startswith("Make Lower"):
        email = email.lower()
        print(email)
    elif command.startswith("GetDomain"):
        command = command.split(" ")
        count = int(command[1])
        part_to_print = email[len(email) - count:]
        print(part_to_print.strip())
    elif command.startswith("GetUsername"):
        if "@" in email:
            index_symbol = email.index("@")
            username = email[:index_symbol]
            print(username)
        else:
            print(f"The email {email} doesn't contain the @ symbol.")
    elif command.startswith("Replace"):
        command = command.split(" ")
        char = command[1]
        email = email.replace(char, "-")
        print(email)
    elif command.startswith("Encrypt"):
        for char in email:
            print(f"{ord(char)}", end=" ")
    command = input().strip()


