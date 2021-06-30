n = int(input())
dictionary = {}

for _ in range(n):
    word = input()
    synonym = input()
    if word not in dictionary:
        dictionary[word] = [synonym]
    else:
        dictionary[word].append(synonym)

for word in dictionary:
    synonyms = ", ".join(dictionary[word])
    print(f"{word} - {synonyms}")