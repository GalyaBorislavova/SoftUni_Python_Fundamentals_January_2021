data = input().split("-")
exam_results = {}
languages = {}

while "exam finished" not in data:
    if "banned" not in data:
        username, language, points = data
        points = int(points)
        if language not in languages:
            languages[language] = 1
        else:
            languages[language] += 1
        if username not in exam_results:
            exam_results[username] = {"Language": language, "Points": points}
        else:
            if exam_results[username]["Points"] < points and exam_results[username]["Language"] == language:
                exam_results[username]["Points"] = points
    else:
        username = data[0]
        for u, l_p in exam_results.items():
            if username in u:
                del exam_results[username]
                break
    data = input().split("-")

print("Results:")
for username, points in sorted(exam_results.items(), key=lambda x: (-x[1]["Points"], x[0])):
    print(f"{username} | {points['Points']}")
print("Submissions:")
for language, count_s in sorted(languages.items(), key=lambda x: (-x[1], x[0])):
    print(f"{language} - {int(count_s)}")