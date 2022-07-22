quantity_of_decorations = int(input())
days_til_xmas = int(input())
cost = 0
spirit = 0
for i in range(1, days_til_xmas + 1):
    if i % 11 == 0:
        quantity_of_decorations += 2
    if i % 2 == 0:
        current_cost = 2 * quantity_of_decorations
        cost += current_cost
        spirit += 5
    if i % 3 == 0:
        current_cost = (5 + 3) * quantity_of_decorations
        cost += current_cost
        spirit += 13
    if i % 5 == 0:
        current_cost = 15 * quantity_of_decorations
        cost += current_cost
        spirit += 17
        if i % 3 == 0:
            spirit += 30
    if i % 10 == 0:
        cost += 23
        spirit -= 20
if days_til_xmas % 10 == 0:
    spirit -= 30

print(f"Total cost: {cost}")

print(f"Total spirit: {spirit}")

