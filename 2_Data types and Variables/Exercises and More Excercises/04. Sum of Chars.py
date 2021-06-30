number = int(input())
sum_chars = 0

for num in range(number):
    n = input()
    sum_chars += ord(n)

print(f"The sum equals: {sum_chars}")
