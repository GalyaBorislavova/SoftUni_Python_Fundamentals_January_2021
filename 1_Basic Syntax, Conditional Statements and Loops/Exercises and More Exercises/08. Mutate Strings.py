first_string = input()
second_string = input()
new_first_string = ""

length = len(second_string)
for i in range(length):
    new_first_string += second_string[i]
    n = new_first_string
    if not first_string[i] == second_string[i]:
        print(n + first_string[i+1::])