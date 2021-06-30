first, second = input().split()

if len(first) <= len(second):
    max_length = len(second)
else:
    max_length = len(first)
total_sum = 0
for index in range(0, max_length):
    if index in range(0, len(first)) and index in range(0, len(second)):
        current_sum = (ord(first[index])) * (ord(second[index]))
        total_sum += current_sum
    else:
        if index in range(0, len(first)):
            for index in range(index, len(first)):
                total_sum += ord(first[index])
            break
        else:
            for index in range(index, len(second)):
                total_sum += ord(second[index])
            break
print(total_sum)
