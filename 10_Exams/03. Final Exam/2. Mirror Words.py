import re

text = input()

pattern_valid_pairs = r"(@{1}|#{1})([A-Za-z]+){3,}(@{2}|#{2})([a-zA-Z]+){3,}(@{1}|#{1})"
valid_pairs = [match.group() for match in re.finditer(pattern_valid_pairs, text)]
if valid_pairs:
    print(f"{len(valid_pairs)} word pairs found!")
else:
    print("No word pairs found!")
mirror_words = []
for word in valid_pairs:
    index_symbol = 0
    if "#" in word:
        index_symbol = word.index("#", 3)
        first_word = word[:index_symbol + 1].replace("#", "")
        second_word = word[index_symbol + 1:].replace("#", "")
        if first_word == second_word[::-1]:
            mirror_words.append(f"{first_word} <=> {second_word}")
    elif "@" in word:
        index_symbol = word.index("@", 3)
        first_word = word[:index_symbol + 1].replace("@", "")
        second_word = word[index_symbol + 1:].replace("@", "")
        if first_word == second_word[::-1]:
            mirror_words.append(f"{first_word} <=> {second_word}")
if mirror_words:
    print(f"The mirror words are:")
    print(f"{', '.join(mirror_words)}")
else:
    print("No mirror words!")

# import re
# text = input()
# pattern = r"(#|@)[A-Za-z]{3,}\1\1[A-Za-z]{3,}\1"
# valid_pairs = [obj.group() for obj in re.finditer(pattern, text)]
# if len(valid_pairs) > 0:
#     print(f"{len(valid_pairs)} word pairs found!")
# else:
#     print("No word pairs found!")
# new_pairs = []
# for pair in valid_pairs:
#     new_pairs.append(pair[1:len(pair) - 1])
# new_valid_pairs = []
# for each in new_pairs:
#     if "#" in each:
#         each = each.split("##")
#     else:
#         each = each.split("@@")
#     first_word = each[0]
#     second_word = each[1]
#     second_word = second_word[::-1]
#     if first_word == second_word:
#         new_valid_pairs.append("".join(each))
# final_list = []
# if len(new_valid_pairs) > 0:
#     print("The mirror words are:")
#     for word in new_valid_pairs:
#         first_word, second_word = word[0:len(word)//2], word[len(word)//2:]
#         final_list.append(f"{first_word} <=> {second_word}")
#     print(", ".join(final_list))
# else:
#     print("No mirror words!")
