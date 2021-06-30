rows = int(input())
game_field = [[int(el) for el in input().split()] for r in range(rows)]

blocks_of_food = 0
coord_to_check = []


def check_neighbour_cells(matrix, list_with_coord):
    row, col = list_with_coord[0][0], list_with_coord[0][1]
    matrix[row][col] = 0
    coord_to_check.pop(0)
    for i, j in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        if 0 <= row + i < len(matrix) and 0 <= col + j < len(matrix[0]) and matrix[row + i][col + j] == 1:
            coord_to_check.append([row + i, col + j])
    if list_with_coord:
        check_neighbour_cells(matrix, list_with_coord)


for row in range(rows):
    for col in range(len(game_field[row])):
        if game_field[row][col] == 1:
            blocks_of_food += 1
            coord_to_check.append([row, col])
            check_neighbour_cells(game_field, coord_to_check)

print(blocks_of_food)
