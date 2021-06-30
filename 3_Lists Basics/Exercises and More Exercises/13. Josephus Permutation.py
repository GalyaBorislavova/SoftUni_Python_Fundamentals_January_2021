permutation = input().split()
step = int(input())

result = []
index = 0
counter = 0

while len(permutation) > 0:
    counter += 1

    if counter % step == 0:
        result.append(permutation.pop(index))
    else:
        index += 1
    if index > len(permutation) - 1:
        index = 0

result_int = []
for el in range(len(result)):
    result_int.append(int(result[el]))

print(str(result_int).replace(" ", ""))
