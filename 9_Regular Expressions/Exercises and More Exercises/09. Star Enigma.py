import re

pattern = r"[ar-t]"
pattern_planets = r"@(?P<name>[A-Za-z]+)([^@\-!:>]+)?:(?P<population>\d+)([^@\-!:>]+)?!(?P<type>[A|D])!([^@\-!:>]+)?->(?P<soldiers>\d+)"
n = int(input())
destroyed_planets = []
attacked_planets = []
for _ in range(n):
    current_command = input()
    match_object = [match_obj.group() for match_obj in re.finditer(pattern, current_command, re.IGNORECASE)]
    if match_object:
        key = len(match_object)
        current_command = [chr(ord(current_command[ind]) - key) for ind in range(0, len(current_command))]
        current_command = ''.join(current_command)
    match = [match.groupdict() for match in re.finditer(pattern_planets, current_command)]
    if match:
        if match[0]["type"] == "A":
            attacked_planets.append(match[0]["name"])
        elif match[0]["type"] == "D":
            destroyed_planets.append(match[0]["name"])

print(f"Attacked planets: {len(attacked_planets)}")
if attacked_planets:
    for planet in sorted(attacked_planets):
        print(f"-> {planet}")
print(f"Destroyed planets: {len(destroyed_planets)}")
if destroyed_planets:
    for planet in sorted(destroyed_planets):
        print(f"-> {planet}")
