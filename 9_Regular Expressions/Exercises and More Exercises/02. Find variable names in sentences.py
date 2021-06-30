import re

pattern = r"(?<= _)[A-Za-z0-9]+($|(?=\s))"
text = input()
valid_variables = [match_obj.group() for match_obj in re.finditer(pattern, text)]
print(*valid_variables, sep=",")