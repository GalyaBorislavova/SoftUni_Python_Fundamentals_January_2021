integer_string = input().split(", ")

integer_list = []
for num in integer_string:
    integer_list.append(int(num))

count_zero = integer_list.count(0)
for zero in range(count_zero):
    index_zero = integer_list.index(0)
    integer_list.pop(index_zero)

for zero_in in range(count_zero):
    integer_list.append(0)

print(integer_list)