factor = int(input())
count = int(input())

numbers = []

for num in range(factor, (factor * count) + 1, factor):
    numbers.append(num)

print(numbers)