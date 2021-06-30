game = [int(x) for x in input().split()]
final_line = len(game) // 2
left_racer = game[:final_line]
right_racer = list(reversed(game[final_line + 1:]))

if left_racer.count(0) > 0:
    zero_position = left_racer.index(0)
    score_left_racer = sum(left_racer[:zero_position]) * 0.8
    score_left_racer += sum(left_racer[zero_position + 1:])
else:
    score_left_racer = sum(left_racer)

if right_racer.count(0) > 0:
    zero_position = right_racer.index(0)
    score_right_racer = sum(right_racer[:zero_position]) * 0.8
    score_right_racer += sum(right_racer[zero_position + 1:])
else:
    score_right_racer = sum(right_racer)

if score_left_racer < score_right_racer:
    print(f"The winner is left with total time: {score_left_racer:.1f}")
else:
    print(f"The winner is right with total time: {score_right_racer:.1f}")

# numbers = [int(el) for el in input().split()]
# middle = int((len(numbers) + 1) / 2)
# left_racer = numbers[0: middle - 1]
# right_racer = numbers[middle:]
# reversed_right_racer = list(reversed(right_racer))
# sum_left_racer = 0
# sum_right_racer = 0
#
# for left in (left_racer):
#     if left == 0:
#         sum_left_racer *= 0.8
#     else:
#         sum_left_racer += left
#
# for right in (reversed_right_racer):
#     if right == 0:
#         sum_right_racer *= 0.8
#     else:
#         sum_right_racer += right
#
# if sum_left_racer < sum_right_racer:
#     print(f"The winner is left with total time: {sum_left_racer:.1f}")
# elif sum_right_racer < sum_left_racer:
#     print(f"The winner is right with total time: {sum_right_racer:.1f}")