import re

pattern_health = r"(?P<health>[^\-\+\*\./0-9])"
pattern_damage = r"(?P<damage>(\-)?\d+(\.)?(\d+)?)"
pattern_count_divide_multiply_symbols = r"(?P<Sign>[/|\*])"

demons_names = [d.strip() for d in input().split(",")]
demons_names = sorted(demons_names)
demons_data = {}
for name in demons_names:
    demons_data[name] = {"Health": 0, "Damage": 0}
    health_symbols = [m.group() for m in re.finditer(pattern_health, name)]
    demons_data[name]["Health"] += sum([ord(h) for h in health_symbols])
    damage_symbols = [d.group() for d in re.finditer(pattern_damage, name)]
    operations = [match_obj.group() for match_obj in re.finditer(pattern_count_divide_multiply_symbols, name)]
    current_sum = sum([float(digit) for digit in damage_symbols])
    if operations:
        for sign in operations:
            if sign == "*":
                current_sum *= 2
            elif sign == "/":
                current_sum /= 2
    demons_data[name]["Damage"] += current_sum

for demon, h_d in demons_data.items():
    print(f"{demon} - {h_d['Health']} health, {h_d['Damage']:.2f} damage")


