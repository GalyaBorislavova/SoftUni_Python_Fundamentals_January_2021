data = input()
emoticons = []

for index, symbol in enumerate(data):
    if symbol == ":" and index + 1 in range(0, len(data)):
        emoticons.append(f"{data[index]}{data[index + 1]}")

print('\n'.join(emoticons))
