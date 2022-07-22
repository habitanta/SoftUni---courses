team_a = ["A-1", "A-2", "A-3", "A-4", "A-5", "A-6", "A-7", "A-8", "A-9", "A-10", "A-11"]
team_b = ["B-1", "B-2", "B-3", "B-4", "B-5", "B-6", "B-7", "B-8", "B-9", "B-10", "B-11"]
termination = False
sent_off_players = input().split()
for player in sent_off_players:
    if player in team_a:
        team_a.remove(player)
    elif player in team_b:
        team_b.remove(player)
    if len(team_a) < 7 or len(team_b) < 7:
        termination = True
        break
print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")
if termination:
    print("Game was terminated")


# ALTERNATE< BUT SLOWER SOLUTION (0.103 vs 0.118 )
# cards = input()
# team_a = 11
# team_b = 11
# terminated = False
# if cards:
#     cards_list = cards.split(' ')
#     sent_off = []
#
#     for card in cards_list:
#         if "A" in card and card not in sent_off:
#             team_a -= 1
#             sent_off.append(card)
#         elif "B" in card and card not in sent_off:
#             team_b -= 1
#             sent_off.append(card)
#         if team_a < 7 or team_b < 7:
#             terminated = True
#             break
# print(f"Team A - {team_a}; Team B - {team_b}")
# if terminated:
#     print("Game was terminated")


