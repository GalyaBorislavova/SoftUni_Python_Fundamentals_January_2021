import re

pattern = r"w{3}\.[A-Za-z0-9-]+(\.[a-z]+)+"

data = input()
valid = []
while data:
    valid_sites = [match.group() for match in re.finditer(pattern, data)]
    if valid_sites:
        valid.extend(valid_sites)
    data = input()

print(*valid, sep="\n")
