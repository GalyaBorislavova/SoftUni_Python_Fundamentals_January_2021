number_of_stars = int(input())

for row in range(1, number_of_stars + 1):
    print(f"*" * row)
for row2 in range(number_of_stars - 1, 0, -1):
    print(f"*" * row2)
