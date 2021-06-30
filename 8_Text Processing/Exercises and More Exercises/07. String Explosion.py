data = list(input())
new_list = []
explosion = 0

for el in data:
    if explosion:
        if el == ">":
            new_list.append(el)
        elif el.isdigit():
            explosion += int(el)
            explosion -= 1
        else:
            explosion -= 1
    else:
        if el.isdigit():
            explosion += int(el)
            explosion -= 1
        else:
            new_list.append(el)

print(*new_list, sep="")









