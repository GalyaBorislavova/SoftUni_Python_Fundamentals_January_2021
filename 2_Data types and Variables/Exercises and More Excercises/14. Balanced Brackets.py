n = int(input())

opening_bracket = 0
closing_bracket = 0

for row in range(n):
    sign = input()
    if sign == "(":
        opening_bracket += 1
    elif sign == ")":
        closing_bracket += 1
        if (opening_bracket - closing_bracket) != 0:
            print("UNBALANCED")
            exit(0)

if opening_bracket == closing_bracket:
    print("BALANCED")
else:
    print("UNBALANCED")