numbers_list = [int(x) for x in input().split(", ")]
index_even_nums = [i for i in range(len(numbers_list)) if numbers_list[i] % 2 == 0]
print(index_even_nums)

