def print_int(num):
    result = num * 2
    print(result)


def print_real(float_num):
    result = float_num * 1.5
    print(f"{result:.2f}")


def print_string(text):
    print(f"${text}$")


data_type = input()
content = input()


if data_type == "int":
    print_int(int(content))
elif data_type == "real":
    print_real(float(content))
elif data_type == "string":
    print_string(content)