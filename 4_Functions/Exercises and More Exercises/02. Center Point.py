x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

coord_A = int(x1), int(y1)
coord_B = int(x2), int(y2)
coord_center = 0, 0


def distance(coord):
    d = abs(coord[0]) + abs(coord[1])
    return d


if distance(coord_A) > distance(coord_B):
    print(coord_B)
elif distance(coord_A) < distance(coord_B):
    print(coord_A)
else:
    print(coord_A)