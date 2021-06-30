command = input()

skills = {}
all_players = {}

while not command == "Season end":
    if "vs" not in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        if player not in skills:
            skills[player] = {position: skill}
            all_players[player] = skill
        else:
            if position not in skills[player]:
                skills[player][position] = skill
                all_players[player] += skill
            else:
                if skills[player][position] < skill:
                    all_players[player] -= skills[player][position]
                    all_players[player] += skill
                    skills[player][position] = skill

    else:
        player_1, player_2 = command.split(" vs ")
        if player_1 in skills and player_2 in skills:
            for key, value in skills[player_1].items():
                if key in skills[player_2].keys():
                    if all_players[player_1] > all_players[player_2]:
                        skills.pop(player_2)
                        all_players.pop(player_2)
                    elif all_players[player_1] < all_players[player_2]:
                        skills.pop(player_1)
                        all_players.pop(player_1)
                    break
    command = input()

sorted_players = dict(sorted(all_players.items(), key=lambda kvp: (-kvp[1], kvp[0])))

for player, total_points in sorted_players.items():
    print(f"{player}: {total_points} skill")

    sorted_skills = dict(sorted(skills[player].items(), key=lambda kvp: (-kvp[1], kvp[0])))
    for position, skill in sorted_skills.items():
        print(f"- {position} <::> {skill}")