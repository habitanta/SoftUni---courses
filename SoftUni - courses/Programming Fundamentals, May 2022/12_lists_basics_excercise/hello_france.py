collection_of_items = input().split("|")
budget = float(input())
train_ticket = 150
clothes_max_price = 50.00
shoes_max_price = 35.00
accessories_max_price = 20.50
new_prices = []
new_budget = 0
profit = 0

for pair in collection_of_items:
    items_in_progress = pair.split("->")
    item = items_in_progress[0]
    price = float(items_in_progress[1])
    if item == "Clothes" and (budget < price or clothes_max_price < price):
        continue
    elif item == "Shoes" and (budget < price or shoes_max_price < price):
        continue
    if item == "Accessories" and (budget < price or accessories_max_price < price):
        continue
    else:
        budget -= price
        profit += (40 * price / 100)
        new_price = (40 * price / 100) + price
        new_prices.append(new_price)
        new_budget += new_price
total_budget = new_budget + budget
for element in new_prices:
    print(f"{element:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")
if total_budget >= train_ticket:
    print("Hello, France!")
else:
    print("Not enough money.")



# ALTERNATE SOLUTION (different way of printing):

# total_budget = new_budget + budget
# new_prices_list = [f"{x:.2f}" for x in new_prices]
# new_prices_print = " ".join(new_prices_list)
# print(new_prices_print)
# print(f"Profit: {profit:.2f}")
# if total_budget >= train_ticket:
#     print("Hello, France!")
# else:
#     print("Not enough money.")

