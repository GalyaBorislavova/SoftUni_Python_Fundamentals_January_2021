import math

party_size = int(input())
days = int(input())

FOOD = 2
WATER = 3
companions_count = party_size
coins_for_companions = 0

for days in range(1, days + 1):
    coins_for_companions += 50
    if days % 10 == 0:
        companions_count -= 2
    if days % 15 == 0:
        companions_count += 5
    coins_for_companions -= FOOD * companions_count
    if days % 3 == 0:
        coins_for_companions -= WATER * companions_count
    if days % 5 == 0:
        coins_for_companions += companions_count * 20
        if days % 3 == 0:
            coins_for_companions -= companions_count * 2

print(f"{companions_count} companions received {math.floor(coins_for_companions / companions_count)} coins each.")