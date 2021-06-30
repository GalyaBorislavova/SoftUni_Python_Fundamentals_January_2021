import re

pattern = r"(?<=(/|\=))(?P<destination>[A-Z][A-Za-z][A-Za-z]([A-Za-z]+)?)(?=\1)"

valid = [match.group() for match in re.finditer(pattern, input())]
travel_points = sum([len(destination) for destination in valid])
print(f"Destinations: {', '.join(valid)}")
print(f"Travel Points: {travel_points}")