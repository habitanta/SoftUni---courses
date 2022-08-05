product_pairs = input().split()
pairs_dict = {product_pairs[i] : product_pairs [i + 1] for i in range(0, len(product_pairs), 2)}
# products_dict = {data[i] : data[i + 1] for i in range(0, len(data), 2)}

search_products = input().split()
for product in search_products:
    if product in pairs_dict:
        print(f"We have {pairs_dict[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")
