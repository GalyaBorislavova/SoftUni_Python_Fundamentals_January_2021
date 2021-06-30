def distance(coord):
    d = abs(coord[0]) + abs(coord[1])
    return d


x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

coord_A = int(x1), int(y1)
coord_B = int(x2), int(y2)
coord_C = int(x3), int(y3)
coord_D = int(x4), int(y4)

first_line = abs(x1) + abs(x2) + abs(y1) + abs(y2)
second_line = abs(x3) + abs(x4) + abs(y3) + abs(y4)

if second_line < first_line:
    if distance(coord_A) <= distance(coord_B):
        print(f"{coord_A}{coord_B}")
    else:
        print(f"{coord_B}{coord_A}")
elif second_line > first_line:
    if distance(coord_C) <= distance(coord_D):
        print(f"{coord_C}{coord_D}")
    else:
        print(f"{coord_D}{coord_C}")
else:
    if distance(coord_A) <= distance(coord_B):
        print(f"{coord_A}{coord_B}")
    else:
        print(f"{coord_B}{coord_A}")
