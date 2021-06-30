word = input()
letters = {}
for ch in range(len(word)):
    if word[ch] != " ":
        if word[ch] in letters:
            letters[word[ch]] += 1
        else:
            letters[word[ch]] = 1

for ch, count in letters.items():
    print(f"{ch} -> {count}")