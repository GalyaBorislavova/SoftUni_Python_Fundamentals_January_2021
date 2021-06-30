from collections import defaultdict


class Dragon:

    def __init__(self, color: str, name: str, damage: int, health: int, armor: int):
        self.color = color
        self.name = name
        self.damage = damage
        self.health = health
        self.armor = armor
        self.id = (name, color)

    def __repr__(self):
        return f"-{self.name} -> damage: {self.damage}, health: {self.health}, armor: {self.armor}"


class Army:

    def __init__(self):
        self.all_dragons = defaultdict(list)

    def add_dragon(self, dragon: Dragon):
        new_dragon = True
        for index, d in enumerate(self.all_dragons[dragon.color]):
            if d.id == dragon.id:
                new_dragon = False
                self.all_dragons[dragon.color].pop(index)
                self.all_dragons[dragon.color].insert(index, dragon)

        if new_dragon:
            self.all_dragons[dragon.color].append(dragon)

    def __repr__(self):
        output = ""
        for color, dragons in self.all_dragons.items():
            average_damage = sum([dragon.damage for dragon in dragons]) / len(dragons)
            average_health = sum([dragon.health for dragon in dragons]) / len(dragons)
            average_armor = sum([dragon.armor for dragon in dragons]) / len(dragons)
            output += f"{color}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})\n"
            for dragon in sorted(dragons, key=lambda x: x.name):
                output += f"-{dragon.name} -> damage: {dragon.damage}, health: {dragon.health}, armor: {dragon.armor}\n"

        return output


def generate_dragon(dragon_data: list):
    color: str = dragon_data[0]
    name: str = dragon_data[1]
    if dragon_data[2] == "null":
        damage: int = 45
    else:
        damage: int = int(dragon_data[2])
    if dragon_data[3] == "null":
        health: int = 250
    else:
        health: int = int(dragon_data[3])
    if dragon_data[4] == "null":
        armor: int = 10
    else:
        armor: int = int(dragon_data[4])

    return Dragon(color, name, damage, health, armor)


dragon_army = Army()
for _ in range(int(input())):
    data = input().split()
    dragon_army.add_dragon(generate_dragon(data))

print(dragon_army)