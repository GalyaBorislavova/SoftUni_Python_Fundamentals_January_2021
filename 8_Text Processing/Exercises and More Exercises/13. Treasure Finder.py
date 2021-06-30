key = [int(i) for i in input().split()]
command = input()

while not command == "find":
    line = command.replace("", " ").split()
    count = 0
    index = 0
    for i, el in enumerate(line):
        line[i] = chr(ord(el) - key[index])
        index += 1
        count += 1
        if index not in range(0, len(key)):
            index = 0
    index_symbols_type = [ind for ind, el in enumerate(line) if el == "&"]
    index_symbols_coordinate = (line.index("<"), line.index(">"))
    print(f"Found {''.join(line[index_symbols_type[0] + 1:index_symbols_type[-1]])} at {''.join(line[index_symbols_coordinate[0] + 1:index_symbols_coordinate[1]])}")
    command = input()
