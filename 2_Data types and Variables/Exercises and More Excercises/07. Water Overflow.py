n = int(input())

CAPACITY_WATER_TANK = 255
full_space = 0

for l in range(n):
    liters = int(input())
    full_space += liters
    if full_space > 255:
        print("Insufficient capacity!")
        full_space -= liters
        continue

print(full_space)
