def valid_user(username):
    is_valid = True
    for letter in username:
        if letter.isdigit() or letter.isalpha() or ord(letter) == 45 or ord(letter) == 95:
            is_valid = True
        else:
            is_valid = False
            return is_valid
    return is_valid


users = input().split(", ")

valid_user_names = []

for user in users:
    if 3 <= len(user) <= 16:
        if valid_user(user):
            valid_user_names.append(user)
        else:
            continue

print('\n'.join(valid_user_names))


# users = input().split(", ")
# for user in users:
#     is_valid = True
#     if 3 <= len(user) <= 16:
#         for letter in user:
#             if ord(letter) == 45 or ord(letter) == 95 or 47 <= ord(letter) <= 57 or 65 <= ord(letter) <= 90 or 97 <= ord(letter) <= 122:
#                 continue
#             else:
#                 is_valid = False
#                 break
#     else:
#         is_valid = False
#     if is_valid:
#         print(user)

