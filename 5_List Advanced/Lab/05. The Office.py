employees = input().split()
factor = int(input())

happiness = [int(h) * factor for h in employees]
avg_happiness = sum(happiness) / len(happiness)
only_happy_people = [int(h) for h in happiness if h > avg_happiness]

if len(only_happy_people) >= len(happiness) // 2:
    print(f"Score: {len(only_happy_people)}/{len(happiness)}. Employees are happy!")
else:
    print(f"Score: {len(only_happy_people)}/{len(happiness)}. Employees are not happy!")