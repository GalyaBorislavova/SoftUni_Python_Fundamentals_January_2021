from collections import defaultdict


class Dwarf:

    def __init__(self, name, hat_color, physics) -> None:
        self.name = name
        self.hat_color = hat_color
        self.physics = physics
        self.group = None
        self.id = (name, hat_color)

    def update_physics(self, new_physics: int):
        self.physics = new_physics

    def set_dwarf_group(self, count: int):
        self.group = count

    def __repr__(self):
        return f"({self.hat_color}) {self.name} <-> {self.physics}"


class OrderDwarfs:

    def __init__(self):
        self.all_dwarfs = []

    def add(self, dwarf: Dwarf):
        new_dwarf = True
        for d in self.all_dwarfs:
            if dwarf.id == d.id:
                new_dwarf = False
                if d.physics < dwarf.physics:
                    d.update_physics(dwarf.physics)

        if new_dwarf:
            self.all_dwarfs.append(dwarf)

    def __repr__(self):
        hat_colors = defaultdict(int)
        for dwarf in self.all_dwarfs:
            hat_colors[dwarf.hat_color] += 1

        for dwarf in self.all_dwarfs:
            dwarf.set_dwarf_group(hat_colors[dwarf.hat_color])

        snow_white_order = []
        for dwarf in sorted(self.all_dwarfs, key=lambda x: (-x.physics, -x.group)):
            snow_white_order.append(f"({dwarf.hat_color}) {dwarf.name} <-> {dwarf.physics}")

        separator = "\n"

        return separator.join(snow_white_order)


order_dwarfs = OrderDwarfs()

while True:
    command = input()
    if command == "Once upon a time":
        break

    dwarf_name, dwarf_hat_color, dwarf_physics = command.split(" <:> ")
    dwarf_physics = int(dwarf_physics)
    order_dwarfs.add(Dwarf(dwarf_name, dwarf_hat_color, dwarf_physics))

print(order_dwarfs)