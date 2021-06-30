numbers = [int(i) for i in input().split(", ")]
group = 10

while numbers:
    current_group = [i for i in numbers if group - 10 <= i <= group]
    print(f"Group of {group}'s: {current_group}")
    for num in current_group:
        numbers.remove(num)
    group += 10
