n = int(input())

positives = []
negatives = []

for _ in range(n):
    number = int(input())
    if number < 0:
        negatives.append(number)
    else:
        positives.append(number)

print(positives)
print(negatives)
print(f"Count of positives: {len(positives)}. Sum of negatives: {sum(negatives)}")
