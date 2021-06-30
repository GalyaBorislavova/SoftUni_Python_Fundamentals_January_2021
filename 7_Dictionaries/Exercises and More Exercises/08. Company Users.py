data = input().split(" -> ")
companies = {}

while "End" not in data:
    name = data[0]
    employee_id = data[1]
    if name not in companies:
        companies[name] = [employee_id]
    else:
        if employee_id not in companies[name]:
            companies[name].append(employee_id)

    data = input().split(" -> ")

for name, employees in sorted(companies.items(), key=lambda x: x[0]):
    print(f"{name}")
    for i in range(len(employees)):
        print(f"-- {employees[i]}")