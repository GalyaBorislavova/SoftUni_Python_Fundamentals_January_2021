n = int(input())

evens = []
odds = []
positives = []
negatives = []

for _ in range(n):
    number = int(input())
    if number % 2 == 0:
        evens.append(number)
    else:
        odds.append(number)
    if number < 0:
        negatives.append(number)
    else:
        positives.append(number)

command = input()

if command == "even":
    print(evens)
elif command == "odd":
    print(odds)
elif command == "positive":
    print(positives)
else:
    print(negatives)
