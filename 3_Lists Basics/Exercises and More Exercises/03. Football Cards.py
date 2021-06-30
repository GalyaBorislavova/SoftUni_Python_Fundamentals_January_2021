cards = input()
cards_list = cards.split(" ")

number_of_players_A = 11
number_of_players_B = 11

out_players_A = []
out_players_B = []
terminated = False

for i in range(len(cards_list)):
    if "A-" in cards_list[i]:
        number_of_players_A -= 1
        if cards_list[i] in out_players_A:
            number_of_players_A += 1
        out_players_A.append(cards_list[i])
    if "B-" in cards_list[i]:
        number_of_players_B -= 1
        if cards_list[i] in out_players_B:
            number_of_players_B += 1
        out_players_B.append(cards_list[i])
    if number_of_players_A < 7 or number_of_players_B < 7:
        terminated = True
        break

print(f"Team A - {number_of_players_A}; Team B - {number_of_players_B}")
if terminated:
    print("Game was terminated")
