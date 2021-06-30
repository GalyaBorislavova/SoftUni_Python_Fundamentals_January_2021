all_events = input().split('|')

energy = 100
coins = 100
is_closed = False

for event in all_events:
    if is_closed:
        break
    event = event.split("-")
    ingredient_or_event = event[0]
    number = int(event[1])
    if ingredient_or_event == "rest":
        if (energy + number) >= 100:
            number = 0
            print(f"You gained {number} energy.")
        else:
            energy += number
            print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")
    elif ingredient_or_event == "order":
        if (energy - 30) >= 0:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
            continue
    else:
        if (coins - number) > 0:
            coins -= number
            print(f"You bought {ingredient_or_event}.")
        else:
            print(f"Closed! Cannot afford {ingredient_or_event}.")
            is_closed = True
            break

if not is_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")