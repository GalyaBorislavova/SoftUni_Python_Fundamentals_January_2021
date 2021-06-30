n = int(input())
special_word = input()

all_words = []

for i in range(n):
    current_string = input()
    all_words.append(current_string)

print(all_words)

for index in range(len(all_words) - 1, -1, -1):
    element = all_words[index]
    if special_word not in element:
        all_words.remove(element)

print(all_words)
