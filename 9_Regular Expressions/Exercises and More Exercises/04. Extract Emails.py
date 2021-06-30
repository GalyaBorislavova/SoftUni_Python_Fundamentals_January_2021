import re

pattern = r"(^|(?<=\s))[A-Za-z0-9]+([\.\-_])?([A-Za-z0-9]+)?@[a-z\-]+\.[a-z]+(\.)?([a-z\-]+)?\b"
data = input()
valid_emails = [match_obj.group() for match_obj in re.finditer(pattern, data)]
print('\n'.join(valid_emails))