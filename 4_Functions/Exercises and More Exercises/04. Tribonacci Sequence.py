num = int(input())
TRIBONACCI_SEQUENCE = 1, 1, 2, 4, 7, 13, 24, 44, 81, 149, 274, 504, 927, 1705, 3136, 5768, 10609, 19513, 35890, 66012, 121415, 223317, 410744, 755476, 1389537, 2555757, 4700770, 8646064, 15902591, 29249425, 53798080, 98950096, 181997601, 334745777, 615693474, 1132436852


def print_tribonacci_sequence(count_number):
    my_sequence = TRIBONACCI_SEQUENCE[:num]
    for nums in range(len(my_sequence)):
        print(my_sequence[nums], end=" ")


print_tribonacci_sequence(num)