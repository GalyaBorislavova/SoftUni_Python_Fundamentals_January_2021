def winner(sign):
    if first_line.count(sign) == 3 or second_line.count(sign) == 3 or third_line.count(sign) == 3:
        return True
    elif first_line[0] == sign and second_line[1] == sign and third_line[2] == sign:
        return True
    elif first_line[2] == sign and second_line[1] == sign and third_line[0] == sign:
        return True
    elif first_line[0] == sign and second_line[0] == sign and third_line[0] == sign:
        return True
    elif first_line[1] == sign and second_line[1] == sign and third_line[1] == sign:
        return True
    elif first_line[2] == sign and second_line[2] == sign and third_line[2] == sign:
        return True
    return False


first_line = [int(el) for el in input().split()]
second_line = [int(el) for el in input().split()]
third_line = [int(el) for el in input().split()]

first_player_sign = 1
second_player_sign = 2
if winner(first_player_sign):
    print("First player won")
elif winner(second_player_sign):
    print("Second player won")
else:
    print("Draw!")
