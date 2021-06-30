substrings = input().split(", ")
words = input().split(", ")
substrings_in = []

for s in range(len(substrings)):
    for w in range(len(words)):
        if substrings[s] in words[w]:
            if not substrings[s] in substrings_in:
                substrings_in.append(substrings[s])

print(substrings_in)