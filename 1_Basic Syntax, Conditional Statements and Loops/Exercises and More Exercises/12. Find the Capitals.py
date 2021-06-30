our_word = input()
word_as_a_list = list(our_word)
positions = []

for i in range(len(our_word)):
    if our_word[i].isupper():
        positions += [i]
print(f"{positions}")