key = int(input())
n = int(input())

result = ""

for i in range(n):
    letter = input()
    descriptive = ord(letter)
    descriptive = descriptive + key
    result += chr(descriptive)

print(f"{result}")


