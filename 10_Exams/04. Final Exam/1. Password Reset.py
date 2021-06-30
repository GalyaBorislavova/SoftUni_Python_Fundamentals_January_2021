# password = input()
# command = input()
# new_password = ""
# while not command == "Done":
#     command = command.split(" ")
#     action = command[0]
#     if action == "TakeOdd":
#         for index in range(0, len(password)):
#             if index % 2 == 1:
#                 new_password += password[index]
#         password = new_password
#         print(password)
#     elif action == "Cut":
#         index, length = [int(i) for i in command[1:]]
#         substring = password[index:index + length]
#         password = password.replace(substring, "", 1)
#         print(password)
#     elif action == "Substitute":
#         substring, substitute = command[1:]
#         if substring in password:
#             password = password.replace(substring, substitute)
#             print(password)
#         else:
#             print("Nothing to replace!")
#     command = input()
#
# print(f"Your password is: {password}")

original_password = input()

command = input()

new_pass = ''

while not command == 'Done':
    if command == 'TakeOdd':
        for index, char in enumerate(original_password):
            if not index % 2 == 0:
                new_pass += char
        original_password = new_pass
        print(new_pass)
    elif command.startswith('Cut'):
        command, ind, lenght = command.split()
        ind = int(ind)
        lenght = int(lenght)
        new_pass = new_pass[:ind] + new_pass[ind+lenght:]
        original_password = new_pass
        print(new_pass)
    elif command.startswith('Substitute'):
        command, substring, substitute = command.split()
        if substring in new_pass:
            new_pass = new_pass.replace(substring, substitute)
            original_password = new_pass
            print(new_pass)
        else:
            print("Nothing to replace!")
    command = input()
print(f'Your password is: {new_pass}')