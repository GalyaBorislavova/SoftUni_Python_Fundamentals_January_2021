def correct_password(pword):
    is_valid = True
    count_nums = 0
    if len(pword) < 6 or len(pword) > 10:
        print("Password must be between 6 and 10 characters")
        is_valid = False
    if not pword.isalnum():
        print("Password must consist only of letters and digits")
        is_valid = False
    for chars in pword:
        if chars.isdigit():
            count_nums += 1
    if count_nums < 2:
        print("Password must have at least 2 digits")
        is_valid = False
    if is_valid:
        print("Password is valid")


password = input()
correct_password(password)