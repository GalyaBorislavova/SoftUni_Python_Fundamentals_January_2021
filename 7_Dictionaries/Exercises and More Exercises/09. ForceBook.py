def add(dict_, our_side, our_user):
    for side, users in our_dict.items():
        if our_user in users:
            return dict_
    if our_side not in dict_:
        dict_[our_side] = []
        dict_[our_side].append(our_user)
    else:
        if our_user not in dict_[our_side]:
            dict_[our_side].append(our_user)
    return dict_


def convert(dict_, our_user, our_side):
    for side, users in dict_.items():
        if our_user in users:
            dict_[side].remove(our_user)
            return add(dict_, our_side, our_user)
    return add(dict_, our_side, our_user)


our_dict = {}
command = input()
while command != "Lumpawaroo":
    if " | " in command:
        side, user = command.split(" | ")
        dict_ = add(our_dict, side, user)
    elif " -> " in command:
        user, side = command.split(" -> ")
        dict_ = convert(our_dict, user, side)
        print(f'{user} joins the {side} side!')
    command = input()

for key, value in sorted(our_dict.items(), key=lambda x: (-len(x[1]), x[0])):
    if len(value) != 0:
        print(f'Side: {key}, Members: {len(value)}')
        for string in sorted(value):
            print(f'! {string}')
