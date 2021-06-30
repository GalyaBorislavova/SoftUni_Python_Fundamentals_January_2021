def exist_index(target_list: list, ind: int):
    if 0 <= ind <= len(target_list) - 1:
        return True
    else:
        return False


def shoot_target(target_list: list, ind: int, p: int):
    if exist_index(target_list, ind):
        target_list[ind] -= p
        if target_list[ind] <= 0:
            target_list.remove(target_list[ind])
        return target_list
    return target_list


def add_target(target_list: list, ind: int, v: int):
    if exist_index(target_list, ind):
        target_list.insert(ind, v)
        return target_list
    else:
        print("Invalid placement!")
        return target_list


def strike_targets(target_list: list, ind: int, r: int):
    if exist_index(target_list, ind - r) and exist_index(target_list, ind + r):
        copy_list = []
        start_index = ind - r
        end_index = ind + r
        copy_list += target_list[: start_index]
        copy_list += target_list[end_index + 1:]
        return copy_list
    else:
        print("Strike missed!")
        return target_list


targets = [int(i) for i in input().split()]
command = input().split()
while "End" not in command:
    index = int(command[1])
    if "Shoot" in command:
        power = int(command[2])
        targets = shoot_target(targets, index, power)
    elif "Add" in command:
        value = int(command[2])
        targets = add_target(targets, index, value)
    elif "Strike" in command:
        radius = int(command[2])
        targets = strike_targets(targets, index, radius)

    command = input().split()

print(*targets, sep="|")