data = input()
contest_with_pass = {}

while not data == "end of contests":
    contest, password = data.split(":")
    contest_with_pass[contest] = password
    data = input()

data = input()
submissions = {}

while not data == "end of submissions":
    contest, password, username, points = data.split("=>")
    points = int(points)
    if contest in contest_with_pass and contest_with_pass[contest] == password:
        if username not in submissions:
            submissions[username] = {contest: points}
        if contest in submissions[username]:
            if submissions[username][contest] < points:
                submissions[username][contest] = points
        else:
            submissions[username][contest] = points
    data = input()

sorted_submissions = {n: v for n, v in (sorted(submissions.items()))}
for key, value in sorted_submissions.items():
    sorted_points = {k: p for k, p in sorted(value.items(), key=lambda x: -x[1])}
    sorted_submissions[key] = sorted_points

max_points = 0
best_candidate = ''

for key, value in sorted_submissions.items():
    current_points = 0
    for c, p in value.items():
        current_points += p
    if current_points > max_points:
        max_points = current_points
        best_candidate = key

print(f"Best candidate is {best_candidate} with total {max_points} points.")
print("Ranking:")
for key, value in sorted_submissions.items():
    print(key)
    for c, p in value.items():
        print(f"#  {c} -> {p}")