n = int(input())
heroes = {}
for _ in range(n):
    data = input().split(" ")
    name = data[0]
    hp, mp = [int(i) for i in data[1:]]
    if name not in heroes:
        if hp <= 100 and mp <= 200:
            heroes[name] = {"HP": hp, "MP": mp}

command = input()
while not command == "End":
    command = command.split(" - ")
    action = command[0]
    if action == "CastSpell":
        hero_name = command[1]
        needed_mp = int(command[2])
        spell = command[3]
        if heroes[hero_name]["MP"] >= needed_mp:
            heroes[hero_name]["MP"] -= needed_mp
            print(f"{hero_name} has successfully cast {spell} and now has {heroes[hero_name]['MP']} MP!")
        else:
            print(f"{hero_name} does not have enough MP to cast {spell}!")
    elif action == "TakeDamage":
        hero_name = command[1]
        damage = int(command[2])
        attacker = command[3]
        heroes[hero_name]["HP"] -= damage
        if heroes[hero_name]["HP"] > 0:
            print(f"{hero_name} was hit for {damage} HP by {attacker} and now has {heroes[hero_name]['HP']} HP left!")
        else:
            del heroes[hero_name]
            print(f"{hero_name} has been killed by {attacker}!")
    elif action == "Recharge":
        hero_name = command[1]
        amount_mp = int(command[2])
        if heroes[hero_name]["MP"] + amount_mp < 200:
            heroes[hero_name]["MP"] += amount_mp
            print(f"{hero_name} recharged for {amount_mp} MP!")
        elif heroes[hero_name]["MP"] + amount_mp == 200:
            heroes[hero_name]['MP'] = 200
            print(f"{hero_name} recharged for {amount_mp} MP!")
        else:
            print(f"{hero_name} recharged for {200 - heroes[hero_name]['MP']} MP!")
            heroes[hero_name]['MP'] = 200

    elif action == "Heal":
        hero_name = command[1]
        amount_hp = int(command[2])
        if heroes[hero_name]["HP"] + amount_hp < 100:
            heroes[hero_name]["HP"] += amount_hp
            print(f"{hero_name} healed for {amount_hp} HP!")
        elif heroes[hero_name]["HP"] + amount_hp == 100:
            heroes[hero_name]["HP"] = 100
            print(f"{hero_name} healed for {amount_hp} HP!")
        else:
            print(f"{hero_name} healed for {100 - heroes[hero_name]['HP']} HP!")
            heroes[hero_name]['HP'] = 100
    command = input()

for hero, hp_mp in sorted(heroes.items(), key=lambda x: (-x[1]['HP'], x[0])):
    print(f"{hero}\n  HP: {hp_mp['HP']}\n  MP: {hp_mp['MP']}")