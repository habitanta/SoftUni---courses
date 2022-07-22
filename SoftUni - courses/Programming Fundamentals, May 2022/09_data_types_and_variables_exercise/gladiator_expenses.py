lost_fights = int(input())
helmet = float(input())
sword = float(input())
shield = float(input())
armor = float(input())
costs = 0
shield_breaks = ""
for i in range(1,lost_fights + 1):
    if i % 2 == 0:
        costs += helmet
    if i % 3 == 0:
        costs += sword
        if i % 2 == 0:
            costs += shield
            shield_breaks += "a"
for num in range(1, len(shield_breaks) + 1):
    if num % 2 == 0:
        costs += armor
print(f"Gladiator expenses: {costs:.2f} aureus")

# ALTERNATE SOLUTION:
# total_helmets_broken = lost_fights // 2
# total_sword_broken = lost_fights // 3
# total_shield_broken = lost_fights // 6      (2 * 3)
# total_armor_broken = total_shield_broken // 2
