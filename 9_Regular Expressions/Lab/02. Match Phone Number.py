import re

pattern = r"\+359(?P<separator>( |-))2(?P=separator)\d{3}(?P=separator)\d{4}\b"

numbers = input()
result = [match_obj.group() for match_obj in re.finditer(pattern, numbers)]
print(', '.join(result))