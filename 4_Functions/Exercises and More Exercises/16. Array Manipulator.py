def exchange(i: int):
    exchanged_numbers = numbers[i:] + numbers[:i]
    return exchanged_numbers


def max_number(nums: list, evens_or_odds: list):
    if not evens_or_odds:
        return "No matches"
    max_num = max(evens_or_odds)
    if nums.count(max_num) > 1:
        index_max_num = len(nums) - 1 - nums[::-1].index(max_num)
        return index_max_num
    else:
        index_max_num = nums.index(max_num)
        return index_max_num


def min_number(nums: list, evens_or_odds: list):
    if not evens_or_odds:
        return "No matches"
    min_num = min(evens_or_odds)
    if nums.count(min_num) > 1:
        index_min_num = len(nums) - 1 - nums[::-1].index(min_num)
        return index_min_num
    else:
        index_min_num = nums.index(min_num)
        return index_min_num


def first_numbers(nums: list, evens_or_odds: list, print_count: int):
    if len(nums) < print_count:
        return "Invalid count"
    if not evens_or_odds:
        return evens_or_odds
    if print_count <= len(evens_or_odds):
        return evens_or_odds[:print_count]
    elif print_count > len(evens_or_odds):
        return evens_or_odds


def last_numbers(evens_or_odds: list, print_count: int):
    if len(numbers) < print_count:
        return "Invalid count"
    if not evens_or_odds:
        return evens_or_odds
    else:
        evens_or_odds = evens_or_odds[::-1]
        list_of_lasts = evens_or_odds[:print_count]
        return list(reversed(list_of_lasts))


numbers = [int(x) for x in input().split()]
command = input().split()

while not command[0] == "end":
    manipulation = command[0]
    if manipulation == "exchange":
        index = int(command[1])
        if 0 <= index < len(numbers):
            numbers = exchange(index + 1)
        else:
            print("Invalid index")
    elif manipulation == "max":
        even_or_odd = command[1]
        if even_or_odd == "even":
            even_nums = [x for x in numbers if x % 2 == 0]
            print(max_number(numbers, even_nums))
        elif even_or_odd == "odd":
            odd_nums = [x for x in numbers if x % 2 == 1]
            print(max_number(numbers, odd_nums))
    elif manipulation == "min":
        even_or_odd = command[1]
        if even_or_odd == "even":
            even_nums = [x for x in numbers if x % 2 == 0]
            print(min_number(numbers, even_nums))
        elif even_or_odd == "odd":
            odd_nums = [x for x in numbers if x % 2 == 1]
            print(min_number(numbers, odd_nums))
    elif manipulation == "first":
        count = int(command[1])
        even_or_odd = command[2]
        if even_or_odd == "even":
            even_nums = [x for x in numbers if x % 2 == 0]
            print(first_numbers(numbers, even_nums, count))
        elif even_or_odd == "odd":
            odd_nums = [x for x in numbers if x % 2 == 1]
            print(first_numbers(numbers, odd_nums, count))
    elif manipulation == "last":
        count = int(command[1])
        even_or_odd = command[2]
        if even_or_odd == "even":
            even_nums = [x for x in numbers if x % 2 == 0]
            print(last_numbers(even_nums, count))
        elif even_or_odd == "odd":
            odd_nums = [x for x in numbers if x % 2 == 1]
            print(last_numbers(odd_nums, count))

    command = input().split()

else:
    print(numbers)