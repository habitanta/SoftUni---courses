command = input().split("|")
energy = 100
coins = 100
managed_all_events = True
for element in command:
    info = element.split("-")
    ingredient = info[0]
    number = int(info[1])
    if "rest" in element:
        if energy + number > 100:
            diff = (energy + number) - 100
            gained_energy = number - diff
            energy = 100
            print(f"You gained {gained_energy} energy.")
            print(f"Current energy: {energy}.")
        elif energy + number <= 100:
            energy += number
            print(f"You gained {number} energy.")
            print(f"Current energy: {energy}.")
    elif "order" in element:
        if energy >= 30:
            coins += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            # if energy > 100:
            #     energy = 100
            print("You had to rest!")
    else:
        if coins >= number:
            coins -= number
            print(f"You bought {ingredient}.")
        else:
            print(f"Closed! Cannot afford {ingredient}.")
            managed_all_events = False
            break
if managed_all_events:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")


# FASTER ALTERNATE SOLUTION (0.070 vs 0.040 s)

# command = input().split("|")
# energy = 100
# coins = 100
# managed_all_events = True
# for element in command:
#     info = element.split("-")
#     ingredient = info[0]
#     number = int(info[1])
#     if "rest" == ingredient:
#         if energy + number > 100:
#             diff = (energy + number) - 100
#             gained_energy = number - diff
#             energy = 100
#             print(f"You gained {gained_energy} energy.")
#             print(f"Current energy: {energy}.")
#         elif energy + number <= 100:
#             energy += number
#             print(f"You gained {number} energy.")
#             print(f"Current energy: {energy}.")
#     elif "order" == ingredient:
#         if energy >= 30:
#             coins += number
#             energy -= 30
#             print(f"You earned {number} coins.")
#         else:
#             energy += 50
#             if energy > 100:
#                 energy = 100
#             print("You had to rest!")
#     else:
#         if coins >= number:
#             coins -= number
#             print(f"You bought {ingredient}.")
#         else:
#             print(f"Closed! Cannot afford {ingredient}.")
#             managed_all_events = False
#             break
# if managed_all_events:
#     print("Day completed!")
#     print(f"Coins: {coins}")
#     print(f"Energy: {energy}")



