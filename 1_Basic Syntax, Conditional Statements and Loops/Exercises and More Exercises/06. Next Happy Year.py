year = int(input())

while True:
    year += 1
    year_as_a_string = str(year)
    if len(year_as_a_string) == len(set(str(year))):
        print(year)
        break