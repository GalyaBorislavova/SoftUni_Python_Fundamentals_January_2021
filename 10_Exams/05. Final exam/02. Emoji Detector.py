import re

pattern_emoji = r"(?<=((:{2})|(\*{2})))(?P<emojis>[A-Z][a-z][a-z]([a-z]+)?)(?=\1)"
pattern_print_emoji = r"((:{2})|(\*{2}))(?P<emojis>[A-Z][a-z][a-z]([a-z]+)?)(\1)"
pattern_nums = r"\d"
result = 1
data = input()
nums_in_data = [int(n) for n in re.findall(pattern_nums, data)]
for num in nums_in_data:
    result *= num
cool_threshold = result
valid_emojis = [match_obj.group() for match_obj in re.finditer(pattern_print_emoji, data)]
cool_emojis = {}
for e in valid_emojis:
    cool = 0
    for letter in e:
        if not letter == ":" and not letter == "*":
            cool += ord(letter)
    if cool >= cool_threshold:
        cool_emojis[e] = cool
print(f"Cool threshold: {cool_threshold}")
print(f"{len(valid_emojis)} emojis found in the text. The cool ones are:")
if cool_emojis:
    print(*cool_emojis, sep='\n')

