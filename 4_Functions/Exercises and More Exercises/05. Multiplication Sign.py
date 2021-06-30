def sign_of_number(num):
    if num < 0:
        return "negative"
    elif num > 0:
        return "positive"
    else:
        return "zero"


num1 = float(input())
num2 = float(input())
num3 = float(input())

signs = sign_of_number(num1), sign_of_number(num2), sign_of_number(num3)

if "zero" in signs:
    print("zero")
elif "positive" in signs and not "negative" in signs:
    print("positive")
elif "negative" in signs and not "positive" in signs:
    print("negative")
elif signs.count("positive") > signs.count("negative"):
    print("negative")
elif signs.count("negative") > signs.count("positive"):
    print("positive")
