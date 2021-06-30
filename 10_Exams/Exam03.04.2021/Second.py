import re

pattern = r"(?<=^)([$%]{1})(?P<tag>[A-Z][a-z][a-z]([a-z]+)*)\1: (\[(?P<digit1>\d+)\]\|)(\[(?P<digit2>\d+)\]\|)(\[(?P<digit3>\d+)\]\|)(?=$)"
n = int(input())
for _ in range(n):
    command = input()
    match = [match_obj.groupdict() for match_obj in re.finditer(pattern, command)]
    if match:
        first = chr(int(match[0]['digit1']))
        second = chr(int(match[0]['digit2']))
        third = chr(int(match[0]['digit3']))
        ascii = first + second + third
        print(f"{match[0]['tag']}: {ascii}")
    else:
        print("Valid message not found!")
