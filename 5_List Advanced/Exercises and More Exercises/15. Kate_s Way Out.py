def get_adjacent_cells(x_coord, y_coord):
    for x, y in [(x_coord + i, y_coord + j) for i in (-1, 0, 1) for j in (-1, 0, 1) if 0 in (i, j)]:
        if lab[x][y] == " ":
            next_move = (x, y)
            return next_move
    return None


rows = int(input())
Exit = ()
lab = [list(input()) for i in range(rows)]
kate = [(row, col) for row in range(rows) for col in range(len(lab[row])) if lab[row][col] == "k"][0]
for row in range(rows):
    for col in range(len(lab[0])):
        if lab[row][col] == " " or lab[row][col] == "k":
            if row == rows - 1 or row == 0 or col == 0 or col == len(lab[row]) - 1:
                Exit = (row, col)
if Exit:
    if kate == Exit:
        print("Kate got out in 1 moves")
    else:
        while True:
            next_step = get_adjacent_cells(kate[0], kate[1])
            if next_step is None:
                print("Kate cannot get out")
                break
            kate = (next_step[0], next_step[1])
            lab[kate[0]][kate[1]] = "k"
            if (kate[0], kate[1]) == Exit:
                print(f"Kate got out in {sum([sub.count('k') for sub in lab])} moves")
                break
else:
    print("Kate cannot get out")
