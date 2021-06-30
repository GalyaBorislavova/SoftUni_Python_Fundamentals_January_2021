import re

pattern = r"(?P<day>\d{2})(?P<separator>[\-\.\/])(?P<month>[A-Z][a-z]{2})(?P=separator)(?P<year>\d{4})"
text = input()
match_dates = [match_obj.groupdict() for match_obj in re.finditer(pattern, text)]
for sub in match_dates:
    print(f"Day: {sub['day']}, Month: {sub['month']}, Year: {sub['year']}")