words = input().split(" ")
decipher = ""

for word in range(len(words)):
    current = words[word]
    new_word = []
    nums_in_word = ""
    for letters in range(len(words[word])):
        if current[letters].isnumeric():
            nums_in_word += current[letters]
        else:
            new_word.append(current[letters])
    new_word.insert(0, chr(int(nums_in_word)))
    new_word[1], new_word[-1] = new_word[-1], new_word[1]
    for l in new_word:
        decipher += l
    if not word == len(words) - 1:
        decipher += " "
print(decipher)
