import re

pattern = r"(^|(?<=\s))(?P<negative>\-)?\d+(?P<floatnumber>\.\d+)?($|(?=\s))"
data = input()
match_nums = [match_obj.group() for match_obj in re.finditer(pattern, data)]
print(*match_nums)