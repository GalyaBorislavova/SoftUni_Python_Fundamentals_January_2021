neighbourhood = [int(i) for i in input().split("@")]
command = input().split()
index_cupid = 0

while "Love!" not in command:
    if "Jump" in command:
        length_jump = int(command[1])
        index_cupid += length_jump
        if 0 <= index_cupid <= len(neighbourhood) - 1:
            if neighbourhood[index_cupid] == 0:
                print(f"Place {index_cupid} already had Valentine's day.")
            else:
                neighbourhood[index_cupid] -= 2
                if neighbourhood[index_cupid] == 0:
                    print(f"Place {index_cupid} has Valentine's day.")
        else:
            index_cupid = 0
            if neighbourhood[index_cupid] == 0:
                print(f"Place {index_cupid} already had Valentine's day.")
            else:
                neighbourhood[index_cupid] -= 2
                if neighbourhood[index_cupid] == 0:
                    print(f"Place {index_cupid} has Valentine's day.")
    command = input().split()

valentine_houses = neighbourhood.count(0)
print(f"Cupid's last position was {index_cupid}.")
if valentine_houses == len(neighbourhood):
    print("Mission was successful.")
else:
    print(f"Cupid has failed {len(neighbourhood) - valentine_houses} places.")

