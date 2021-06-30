word = input()
result = 0
special_keys = ["sun", "water", "sand", "fish"]

for i in range(len(special_keys)):
    result += word.lower().count(special_keys[i])

print(result)