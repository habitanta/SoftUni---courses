number_of_orders = int(input())
total_price = 0
for n in range(number_of_orders):
    price_per_capsule = float(input())
    days = int(input())
    capsules = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100.00:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules < 1 or capsules > 2000:
        continue
    price_per_order = capsules * price_per_capsule * days
    total_price += price_per_order
    print(f"The price for the coffee is: ${price_per_order:.2f}")
print(f"Total: ${total_price:.2f}")



number_of_orders = int(input())
total_price = 0
for order in range(number_of_orders):
    capsule_price = float(input())
    days = int(input())
    amount_of_capsules = int(input())
    if capsule_price < 0.01 or capsule_price > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif amount_of_capsules < 1 or amount_of_capsules > 2000:
        continue
    current_order_price = capsule_price * amount_of_capsules * days
    total_price += current_order_price
    print(f"The price for the coffee is: ${current_order_price:.2f}")
print(f"Total: ${total_price:.2f}")
