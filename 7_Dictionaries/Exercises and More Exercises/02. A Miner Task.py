resource = input()
miner_task = {}

while not resource == "stop":
    quantity = int(input())
    if resource in miner_task:
        miner_task[resource] += quantity
    else:
        miner_task[resource] = quantity
    resource = input()

for resource, quantity in miner_task.items():
    print(f"{resource} -> {quantity}")