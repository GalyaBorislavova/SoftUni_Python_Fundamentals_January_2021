data = input().split()
words = {}

for word in data:
    word = word.lower()
    if word not in words:
        words[word] = 1
    else:
        words[word] += 1

for item, quantity in words.items():
    if quantity % 2 == 1:
        print(item, end=" ")
