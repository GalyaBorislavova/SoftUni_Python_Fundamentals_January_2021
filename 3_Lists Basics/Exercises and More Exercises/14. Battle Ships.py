number_of_rows = int(input())

dead = 0
all_game = []
for rows in range(number_of_rows):
    current_row = input().split()
    all_game.append(current_row)
attack = input().split(" ")
for i in attack:
    row = int(i[0])
    col = int(i[2])
    if int(all_game[row][col]) > 0:
        all_game[row][col] = int(all_game[row][col]) - 1
        if int(all_game[row][col]) == 0:
            dead += 1
print(dead)
