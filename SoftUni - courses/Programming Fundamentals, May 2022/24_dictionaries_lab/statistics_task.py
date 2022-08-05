
products_dict = {}

while True:
    command = input().split(": ")
    if command[0] == "statistics":
        break
    else:
        product = command[0]
        quantity = int(command[1])
        if product not in products_dict:
            products_dict[product] = quantity
        else:
            products_dict[product] += quantity
print("Products in stock:" )
for key, value in products_dict.items():
    print(f"- {key}: {value}")
# ALTERNATE WRITING:
# product_representation = [f"- {item}: {str(products_dict[item])}" for item in products_dict]
# print("\n".join(product_representation))

print(f"Total Products: {len(products_dict)}")
print(f"Total Quantity: {sum(products_dict.values())}")
